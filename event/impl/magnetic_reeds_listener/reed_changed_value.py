from config.event_conf import EventConf
from event.base_event import BaseEvent
from event.impl.magnetic_reeds_listener.enums.status import Status


class ReedChangedValue(BaseEvent):
    def __init__(self, gpio_pin_number: int, status: Status):
        super().__init__(EventConf.REED_CHANGED_VALUE)
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
