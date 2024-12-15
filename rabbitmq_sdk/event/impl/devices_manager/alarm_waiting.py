from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent


class AlarmWaiting(BaseEvent):
    def __init__(self, started: bool, timestamp: int):
        super().__init__(Service.DEVICES_MANAGER, Event.ALARM_WAITING)
        self.started = started
        self.timestamp = timestamp

    def to_dict(self):
        event_dict = {
            "started": self.started,
            "timestamp": self.timestamp
        }
        return event_dict

    @classmethod
    def from_dict(cls, data):
        started = bool(data["started"])
        timestamp = int(data["timestamp"])
        return cls(started, timestamp)

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self._timestamp = value

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value: bool):
        self._started = value