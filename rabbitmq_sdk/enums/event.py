from enum import Enum, auto


class Event(Enum):
    CAMERA_ALARM = auto(),
    REED_ALARM = auto(),
    ALARM_STOPPED = auto()

    def get_name(self):
        return self.name