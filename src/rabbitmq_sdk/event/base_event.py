from abc import ABC, abstractmethod

from src.rabbitmq_sdk.config.event_conf import EventConf


class BaseEvent(ABC):
    @abstractmethod
    def __init__(self, configuration: EventConf):
        if configuration is None:
            raise ValueError("Configuration cannot be null")
        if not isinstance(self, configuration.get_event_class()):
            raise RuntimeError(
                "Invalid configuration: instantiating event different from class specified in its configuration"
            )
        self.event_config = configuration

    @property
    def service_from(self):
        return self.event_config.get_service_from()

    @property
    def event_name(self):
        return self.event_config.get_event_name()