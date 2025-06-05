from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from time import sleep


red_light = Led_Light(3, False)
ped_button = Pedestrian_Button(22, False)

while True:
    red_light.led_light_state = ped_button.button_state
    sleep(5)