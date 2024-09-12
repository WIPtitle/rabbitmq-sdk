from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent
from rabbitmq_sdk.event.impl.devices_manager.enums.reed_status import ReedStatus


class ReedChangedStatus(BaseEvent):
    def __init__(self, gpio_pin_number: int, status: ReedStatus, timestamp: int):
        super().__init__(Service.DEVICES_MANAGER, Event.REED_CHANGED_STATUS)
        self.gpio_pin_number = gpio_pin_number
        self.status = status
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "gpio_pin_number": self.gpio_pin_number,
            "status": self.status.value,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        gpio_pin_number = data["gpio_pin_number"]
        status = ReedStatus(data["status"])
        timestamp = int(data["timestamp"])
        return cls(gpio_pin_number, status, timestamp)

    @property
    def gpio_pin_number(self):
        return self._gpio_pin_number

    @gpio_pin_number.setter
    def gpio_pin_number(self, value: int):
        self._gpio_pin_number = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: ReedStatus):
        self._status = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self._timestamp = value
