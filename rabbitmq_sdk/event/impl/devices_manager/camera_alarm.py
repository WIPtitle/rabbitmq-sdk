import base64

from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent


class CameraAlarm(BaseEvent):
    def __init__(self, name: str, blob: bytes, timestamp: int):
        super().__init__(Service.DEVICES_MANAGER, Event.CAMERA_ALARM)
        self.name = name
        self.blob = blob
        self.timestamp = timestamp

    def to_dict(self):
        event_dict = {
            "name": self.name,
            "timestamp": self.timestamp
        }
        if self.blob is not None:
            event_dict["blob"] = base64.b64encode(self.blob).decode('utf-8')
        return event_dict

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        blob = base64.b64decode(data["blob"]) if "blob" in data else None
        timestamp = int(data["timestamp"])
        return cls(name, blob, timestamp)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def blob(self):
        return self._blob

    @blob.setter
    def blob(self, value: bytes):
        self._blob = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self._timestamp = value