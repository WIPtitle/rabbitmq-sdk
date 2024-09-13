import json
import logging
from abc import abstractmethod, ABC
from typing import Type

from rabbitmq_sdk.consumer.utils.custom_default_consumer import CustomDefaultConsumer
from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.event.base_event import BaseEvent


class BaseConsumer(CustomDefaultConsumer, ABC):
    def __init__(self, channel=None):
        super().__init__(channel)
        self.logger = logging.getLogger(self.__class__.__name__)


    def close(self):
        self.channel.basic_cancel(self.consumer_tag)


    def handle_delivery(self, channel, method, properties, body):
        try:
            print("Received an event")
            message = body.decode('utf-8')
            data = json.loads(message)
            self.do_handle(BaseEvent.from_dict(data))
            self.send_ack(method.delivery_tag)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print("Can't process entity in queue", e)
        except Exception as e:
            print("Can't send ack back to rabbitmq", e)


    def send_ack(self, delivery_tag):
        self.channel.basic_ack(delivery_tag)


    @abstractmethod
    def get_event(self) -> Event:
        pass


    @abstractmethod
    def event_class(self) -> Type[BaseEvent]:
        pass


    @abstractmethod
    def do_handle(self, event: BaseEvent):
        pass