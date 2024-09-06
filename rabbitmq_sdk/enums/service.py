from enum import Enum, auto


class Service(Enum):
    MAGNETIC_REEDS_LISTENER = auto(),
    RTSP_CAMERAS_LISTENER = auto()