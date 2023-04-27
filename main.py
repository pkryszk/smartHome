import sys
import os

iot_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'iot'))
sys.path.append(iot_path)

from iot.service import IOTService as IOTService
from iot.devices import HueLight as HueLight
from iot.devices import SmartSpeaker as SmartSpeaker
from iot.devices import Curtains as Curtains

from iot.message import Message as Message
from iot.message import MessageType as MessageType



def main():
    # tworzy instancję IOTService
    iot_service = IOTService()

    #tworzy instancje dostępnych urządzeń
    hue_light = HueLight()
    smart_speaker_1 = SmartSpeaker()
    smart_speaker_2 = SmartSpeaker()
    curtains = Curtains()

    # rejestruje urządzenia
    hue_light_device_id=iot_service.register_device(hue_light)
    smart_speaker_1_device_id = iot_service.register_device(smart_speaker_1)
    smart_speaker_2_device_id= iot_service.register_device(smart_speaker_2)
    curtains_device_id = iot_service.register_device(curtains)

    # testuje urządzenia
    iot_service.test_devices()

    # tworzy programy (listy Message)
    wake_up = list()
    wake_up.append(Message(hue_light_device_id,MessageType.SWITCH_ON,"włączam światła"))
    wake_up.append(Message(smart_speaker_1_device_id, MessageType.SWITCH_ON, "włączam głośnik w sypialni"))
    wake_up.append(Message(smart_speaker_2_device_id, MessageType.SWITCH_ON, "włączam głośnik w łazience"))
    wake_up.append(Message(smart_speaker_1_device_id, MessageType.PLAY_SONG, "włączam piosenkę w sypialni"))
    wake_up.append(Message(smart_speaker_2_device_id, MessageType.PLAY_SONG, "włączam piosenkę w łazience"))
    wake_up.append(Message(curtains_device_id, MessageType.OPEN, "Otwieram zasłony"))

    sleep = list()
    sleep.append(Message(hue_light_device_id,MessageType.SWITCH_OFF,"wyłączam światła"))
    sleep.append(Message(smart_speaker_1_device_id, MessageType.SWITCH_OFF, "wyłączam głośnik w sypialni"))
    sleep.append(Message(smart_speaker_2_device_id, MessageType.SWITCH_OFF, "wyłączam głośnik w łazience"))
    sleep.append(Message(curtains_device_id, MessageType.CLOSE, "zamykam zasłony"))

    # uruchamia programy
    iot_service.run_program(wake_up)
    iot_service.run_program(sleep)

   # usuwa urządzenia
    iot_service.unregister_device(hue_light_device_id)
    iot_service.unregister_device(smart_speaker_1_device_id)
    iot_service.unregister_device(smart_speaker_2_device_id)
    iot_service.unregister_device(curtains_device_id)

   #konczy program

if __name__ == '__main__':
    main()

