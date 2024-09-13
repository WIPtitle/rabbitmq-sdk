import base64

from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent


class AlarmStopped(BaseEvent):
    def __init__(self, timestamp: int):
        super().__init__(Service.DEVICES_MANAGER, Event.ALARM_STOPPED)
        self.timestamp = timestamp

    def to_dict(self):
        event_dict = {
            "timestamp": self.timestamp
        }
        return event_dict

    @classmethod
    def from_dict(cls, data):
        timestamp = int(data["timestamp"])
        return cls(timestamp)

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self._timestamp = value