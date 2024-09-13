from enum import Enum, auto


class Service(Enum):
    DEVICES_MANAGER = auto(),
    AUDIO_MANAGER = auto(),
    MAIL_NOTIFICATION = auto()