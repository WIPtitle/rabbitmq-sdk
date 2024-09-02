from enum import Enum, auto


class Event(Enum):
    REED_CHANGED_VALUE = auto()

    def get_name(self):
        return self.name