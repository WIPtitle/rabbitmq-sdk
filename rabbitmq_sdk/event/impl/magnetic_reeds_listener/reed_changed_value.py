from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent
from rabbitmq_sdk.event.impl.magnetic_reeds_listener.enums.status import Status


class ReedChangedValue(BaseEvent):
    def __init__(self, gpio_pin_number: int, status: Status):
        super().__init__(Service.MAGNETIC_REEDS_LISTENER, Event.REED_CHANGED_VALUE)
        self.gpio_pin_number = gpio_pin_number
        self.status = status

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
