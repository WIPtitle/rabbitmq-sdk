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
        self.get_channel().basic_cancel(self.consumer_tag)


    def handle_delivery(self, channel, method, properties, body):
        message = body.decode('utf-8')
        data = json.loads(message)
        try:
            self.do_handle(data)
            channel.basic_ack(method.delivery_tag)
        except Exception as e:
            self.logger.error(f"Error handling message: {e}")
            channel.basic_nack(method.delivery_tag)


    @abstractmethod
    def get_event(self) -> Event:
        pass


    @abstractmethod
    def event_class(self) -> Type[BaseEvent]:
        pass


    @abstractmethod
    def do_handle(self, event):
        pass