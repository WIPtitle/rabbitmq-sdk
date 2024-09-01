from enum import Enum

class Service(Enum):
    MAGNETIC_REEDS_LISTENER = "MAGNETIC_REEDS_LISTENER"
    PROJECT_CORE = "PROJECT_CORE"

    def get_service_name(self):
        return self.name
