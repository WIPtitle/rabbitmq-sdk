from enum import Enum

from config.service import Service
from event.impl.magnetic_reeds_listener.reed_changed_value import ReedChangedValue


class EventConf(Enum):
    REED_CHANGED_VALUE = (Service.MAGNETIC_REEDS_LISTENER, ReedChangedValue)


    def __init__(self, service_from, event_class):
        self.service_from = service_from
        self.event_class = event_class

    def get_event_name(self):
        return self.name

    def get_service_from(self):
        return self.service_from

    def get_event_class(self):
        return self.event_class