import device
from iot.message import MessageType


class HueLight(device.Device):
    def connect(self) -> None:
        print(f"Connecting {__class__.__name__}")

    def disconnect(self) -> None:
        print(f"Disconnect {__class__.__name__}")

    def send_message(self, message_type: MessageType, data: str):
        print(f"Hue light handling message of type {message_type.name} with data [{data}].")

    def status_update(self) -> str:
        print(f"hue_light_status_ok")


class SmartSpeaker(device.Device):
    def connect(self) -> None:
        print(f"Connecting {__class__.__name__}")

    def disconnect(self) -> None:
        print(f"Disconnect {__class__.__name__}")

    def send_message(self, message_type: MessageType, data: str):
        print(f"{__class__.__name__} handling message of type {message_type.name} with data [{data}].")

    def status_update(self) -> str:
        print(f"{__class__.__name__}_status_ok")


class Curtains(device.Device):
    def connect(self) -> None:
        print(f"Connecting {__class__.__name__}")

    def disconnect(self) -> None:
        print(f"Disconnect {__class__.__name__}")

    def send_message(self, message_type: MessageType, data: str):
        print(f"{__class__.__name__} handling message of type {message_type.name} with data [{data}].")

    def status_update(self) -> str:
        print(f"{__class__.__name__}_status_ok")
