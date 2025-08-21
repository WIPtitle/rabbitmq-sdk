from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent


class SensorAlarm(BaseEvent):
    def __init__(self, sensor_name: str, timestamp: int):
        super().__init__(Service.DEVICES_MANAGER, Event.SENSOR_ALARM)
        self.sensor_name = sensor_name
        self.timestamp = timestamp

    def to_dict(self):
        event_dict = {
            "sensor_name": self.sensor_name,
            "timestamp": self.timestamp
        }
        return event_dict

    @classmethod
    def from_dict(cls, data):
        sensor_name = str(data["sensor_name"])
        timestamp = int(data["timestamp"])
        return cls(sensor_name, timestamp)

    @property
    def sensor_name(self):
        return self._sensor_name

    @sensor_name.setter
    def sensor_name(self, value: str):
        self._sensor_name = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self._timestamp = value