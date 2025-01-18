from enum import Enum, auto


class Event(Enum):
    REED_ALARM = auto(),
    ALARM_STOPPED = auto(),
    ALARM_WAITING = auto(),

    def get_name(self):
        return self.name