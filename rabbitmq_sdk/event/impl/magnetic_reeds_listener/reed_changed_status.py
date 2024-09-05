from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent
from rabbitmq_sdk.event.impl.magnetic_reeds_listener.enums.status import Status


class ReedChangedStatus(BaseEvent):
    def __init__(self, gpio_pin_number: int, status: Status):
        super().__init__(Service.MAGNETIC_REEDS_LISTENER, Event.REED_CHANGED_STATUS)
        self.gpio_pin_number = gpio_pin_number
        self.status = status

    def to_dict(self):
        return {
            "gpio_pin_number": self.gpio_pin_number,
            "status": self.status.value
        }

    @classmethod
    def from_dict(cls, data):
        gpio_pin_number = data["gpio_pin_number"]
        status = Status(data["status"])
        return cls(gpio_pin_number, status)

    @property
    def gpio_pin_number(self):
        return self._gpio_pin_number

    @gpio_pin_number.setter
    def gpio_pin_number(self, value):
        self._gpio_pin_number = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
