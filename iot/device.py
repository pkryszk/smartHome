from message import MessageType
from abc import ABC, abstractmethod


class Device(ABC):

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send_message(self, message_type: MessageType, data: str):
        pass

    @abstractmethod
    def status_update(self) -> str:
       pass
