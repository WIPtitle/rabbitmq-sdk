from abc import ABC, abstractmethod

from consumer.base_consumer import BaseConsumer
from event.base_event import BaseEvent


class RabbitMQClient(ABC):
    @abstractmethod
    def publish(self, base_event: BaseEvent):
        pass

    @abstractmethod
    def consume(self, consumer: BaseConsumer):
        pass