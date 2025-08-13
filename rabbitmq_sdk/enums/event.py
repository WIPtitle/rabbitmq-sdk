from enum import Enum, auto


class Event(Enum):
    ALARM_STOPPED = auto(),
    ALARM_WAITING = auto(),
    SENSOR_ALARM = auto(),

    def get_name(self):
        return self.name