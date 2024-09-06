from enum import Enum, auto


class Event(Enum):
    REED_CHANGED_STATUS = auto(),
    CAMERA_CHANGED_STATUS = auto()

    def get_name(self):
        return self.name