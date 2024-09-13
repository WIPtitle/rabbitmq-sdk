from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent


class ReedAlarm(BaseEvent):
    def __init__(self, name: str, timestamp: int):
        super().__init__(Service.DEVICES_MANAGER, Event.REED_ALARM)
        self.name = name
        self.timestamp = timestamp

    def to_dict(self):
        event_dict = {
            "name": self.name,
            "timestamp": self.timestamp
        }
        return event_dict

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        timestamp = int(data["timestamp"])
        return cls(name, timestamp)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self._timestamp = value