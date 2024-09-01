from abc import ABC, abstractmethod

from src.consumer.base_consumer import BaseConsumer
from src.event.base_event import BaseEvent


class RabbitMQClient(ABC):
    @abstractmethod
    def publish(self, base_event: BaseEvent):
        pass

    @abstractmethod
    def consume(self, consumer: BaseConsumer):
        pass