import json
import logging
from abc import abstractmethod, ABC

from src.rabbitmq_sdk.config.event_conf import EventConf
from src.rabbitmq_sdk.consumer.utils.custom_default_consumer import CustomDefaultConsumer


class BaseConsumer(CustomDefaultConsumer, ABC):
    def __init__(self, channel=None):
        super().__init__(channel)
        self.logger = logging.getLogger(self.__class__.__name__)

    def close(self):
        self.channel.basic_cancel(self.consumer_tag)

    def handle_delivery(self, channel, method, properties, body):
        try:
            self.logger.info("Received an event")
            message = body.decode('utf-8')
            event = json.loads(message, object_hook=self.event_class())
            self.do_handle(event)
            self.send_ack(method.delivery_tag)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            self.logger.error("Can't process entity in queue", e)
        except Exception as e:
            self.logger.error("Can't send ack back to rabbitmq", e)

    def send_ack(self, delivery_tag):
        self.channel.basic_ack(delivery_tag)

    @property
    def event_name(self):
        return self.get_event_config().get_event_name()

    @property
    def event_class(self):
        return self.get_event_config().get_event_class()

    @abstractmethod
    def get_event_config(self) -> EventConf:
        pass

    @abstractmethod
    def do_handle(self, event):
        pass