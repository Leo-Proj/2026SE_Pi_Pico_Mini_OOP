from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep

button = Pedestrian_Button(27, True)
buzzer = Audio_Notification(27, True)

while True:
    if button.value():
        buzzer.beep(freq=freq, duration=100)
        freq += 15
    else:
        buzzer.duty_u16(0)
    sleep(0.05)


# while True:
#     red_light.led_light_state = ped_button.button_state
#     sleep(5)