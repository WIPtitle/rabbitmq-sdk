from abc import ABC, abstractmethod

from rabbitmq_sdk.consumer.base_consumer import BaseConsumer
from rabbitmq_sdk.event.base_event import BaseEvent


class RabbitMQClient(ABC):
    @abstractmethod
    def publish(self, base_event: BaseEvent):
        pass

    @abstractmethod
    def consume(self, consumer: BaseConsumer):
        pass