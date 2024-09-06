from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent
from rabbitmq_sdk.event.impl.rtsp_cameras_listener.enums.camera_status import CameraStatus


class CameraChangedStatus(BaseEvent):
    def __init__(self, ip: str, status: CameraStatus):
        super().__init__(Service.RTSP_CAMERAS_LISTENER, Event.CAMERA_CHANGED_STATUS)
        self.ip = ip
        self.status = status

    def to_dict(self):
        return {
            "ip": self.ip,
            "status": self.status.value
        }

    @classmethod
    def from_dict(cls, data):
        gpio_pin_number = data["ip"]
        status = CameraStatus(data["status"])
        return cls(gpio_pin_number, status)

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value: str):
        self._ip = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: CameraStatus):
        self._status = value
