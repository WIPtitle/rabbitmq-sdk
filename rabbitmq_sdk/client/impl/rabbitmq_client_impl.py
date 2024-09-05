import json
import logging
import pika
from pika.exceptions import UnroutableError

from rabbitmq_sdk.client.rabbitmq_client import RabbitMQClient
from rabbitmq_sdk.consumer.base_consumer import BaseConsumer
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent


def get_exchange_name(event_name):
    return f"{event_name}_EXCHANGE"


def get_queue_name(event_name, service_to_name):
    return f"{event_name}_{service_to_name}_QUEUE"


class RabbitMQClientImpl(RabbitMQClient):
    def __init__(self, connection_params):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.connection_params = connection_params
        self.connection = None
        self.publishing_channel = None
        self.current_service = None


    @classmethod
    def from_config(cls, host, port, username, password):
        connection_params = pika.ConnectionParameters(
            host=host,
            port=port,
            credentials=pika.PlainCredentials(username, password)
        )
        return cls(connection_params)


    def with_current_service(self, current_service: Service):
        self.current_service = current_service
        return self


    def is_current_service_set(self):
        return self.current_service is not None


    def new_channel(self):
        return self.connection.channel()


    def init_connection(self):
        if self.connection is None or self.connection.is_closed:
            try:
                self.connection = pika.BlockingConnection(self.connection_params)
            except Exception as e:
                raise RuntimeError("Can't connect to RabbitMQ") from e


    def init_publishing_channel(self):
        if self.publishing_channel is None or self.publishing_channel.is_closed:
            try:
                self.publishing_channel = self.connection.channel()
            except Exception as e:
                raise RuntimeError("Could not create RabbitMQ channel for websocket") from e


    def init_connection_and_publishing_channel(self):
        self.init_connection()
        self.init_publishing_channel()


    def publish(self, base_event: BaseEvent):
        self.init_connection_and_publishing_channel()
        if not self.is_current_service_set():
            self.logger.error(
                "Current service not set, use with_current_service to set it before trying to publish an event"
            )
            return False

        if base_event.get_service_from() != self.current_service:
            self.logger.error(
                "Event service_from does not match current service, are you publishing the right event from the right service?"
            )
            return False

        try:
            self.publishing_channel.confirm_delivery()

            exchange_name = get_exchange_name(base_event.get_event().get_name())
            self.logger.info(f"Declaring exchange {exchange_name}")
            self.publishing_channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)

            self.logger.info("Trying to publish message")
            message = json.dumps(base_event.to_dict())

            try:
                self.publishing_channel.basic_publish(
                    exchange=exchange_name,
                    routing_key='',
                    body=message,
                    properties=pika.BasicProperties(delivery_mode=2)
                )
            except UnroutableError as e:
                self.logger.error(f"Could not publish message", e)
                return False

            return True

        except json.JSONDecodeError as e:
            self.logger.error("JSON error while publishing message", e)
            return False
        except Exception as e:
            self.logger.error("Exception while publishing message", e)
            return False

    def consume(self, base_consumer: BaseConsumer):
        self.init_connection_and_publishing_channel()
        if not self.is_current_service_set():
            self.logger.error(
                "Current service not set, use with_current_service to set it before trying to start a consumer"
            )
            return False

        self.logger.info("Starting consumer")
        channel = self.new_channel()
        base_consumer.channel = channel

        try:
            exchange_name = get_exchange_name(base_consumer.get_event().get_name())
            self.logger.info(f"Declaring exchange {exchange_name}")
            self.publishing_channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)

            queue_name = get_queue_name(base_consumer.get_event().get_name(), self.current_service.name)
            self.logger.info(f"Declaring queue {queue_name}")
            channel.queue_declare(queue=queue_name, durable=True)

            channel.queue_bind(queue=queue_name, exchange=exchange_name)

            channel.basic_consume(queue=queue_name, on_message_callback=base_consumer.handle_delivery, auto_ack=False)

            return True
        except Exception as e:
            self.logger.error("Can't consume from queue", e)
            return False