from enum import Enum


class CameraStatus(Enum):
    MOVEMENT_DETECTED = "MOVEMENT_DETECTED"
    IDLE = "IDLE"
    UNREACHABLE = "UNREACHABLE"