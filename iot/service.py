from device import Device as Device
from message import Message as Message
import random
import string
import diagnostics


def generate_id(length: int) -> str:
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))


class IOTService:
    __DEVICE_ID_LENGTH = 8

    def __init__(self):
        # tworzę dict mimo iż w treści zadania bylo "dodaje urządzenie do listy 'devices'"
        self.__devices = dict()

    def register_device(self, d: Device) ->str:
        d.connect()
        device_id = generate_id(IOTService.__DEVICE_ID_LENGTH)
        while device_id in self.__devices:
            device_id = generate_id(IOTService.__DEVICE_ID_LENGTH)
        self.__devices[device_id] = d
        # zwracam device_id mimo, że nie było takiego wymagania w treści zadania
        return device_id

    def unregister_device(self, device_id: str):
        if device_id in self.__devices:
            self.__devices[device_id].disconnect()
            del self.__devices[device_id]

    # ta metoda nie jest nigdzie wykorzystywana
    def get_device(self, device_id: str) -> Device:
        if device_id in self.__devices:
            return self.__devices[device_id]

    def run_program(self, lst: [Message]):
        print('"=====RUNNING PROGRAM======"')
        for m in lst:
            self.__devices[m.device_id].send_message(m.msg_type, m.data)
        print('"=====END OF PROGRAM======"')

    def test_devices(self):
        print("Start test devices")
        for v in self.__devices.values():
            diagnostics.collect_diagnostics(v)
