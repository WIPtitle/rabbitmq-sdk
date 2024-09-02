from abc import ABC, abstractmethod

from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service


class BaseEvent(ABC):
    @abstractmethod
    def __init__(self, service: Service, event: Event):
        self.service = service
        self.event = event

    def get_service_from(self) -> Service:
        return self.service

    def get_event(self) -> Event:
        return self.event