import base64

from rabbitmq_sdk.enums.event import Event
from rabbitmq_sdk.enums.service import Service
from rabbitmq_sdk.event.base_event import BaseEvent
from rabbitmq_sdk.event.impl.rtsp_cameras_listener.enums.camera_status import CameraStatus


class CameraChangedStatus(BaseEvent):
    def __init__(self, ip: str, status: CameraStatus, blob: bytes | None = None):
        super().__init__(Service.RTSP_CAMERAS_LISTENER, Event.CAMERA_CHANGED_STATUS)
        self.ip = ip
        self.status = status
        self.blob = blob

    def to_dict(self):
        event_dict = {
            "ip": self.ip,
            "status": self.status.value
        }
        if self.blob is not None:
            event_dict["blob"] = base64.b64encode(self.blob).decode('utf-8')
        return event_dict

    @classmethod
    def from_dict(cls, data):
        ip = data["ip"]
        status = CameraStatus(data["status"])
        blob = base64.b64decode(data["blob"]) if "blob" in data else None
        return cls(ip, status, blob)

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

    @property
    def blob(self):
        return self._blob

    @blob.setter
    def blob(self, value: bytes):
        self._blob = value