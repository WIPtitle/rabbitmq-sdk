from dataclasses import dataclass
from rabbitmq_sdk.event.base_event import BaseEvent


@dataclass
class SensorAlarm(BaseEvent):
    """Event emitted when a sensor triggers an alarm"""
    sensor_name: str
    timestamp: int

    def __init__(self, sensor_name: str, timestamp: int):
        self.sensor_name = sensor_name
        self.timestamp = timestamp