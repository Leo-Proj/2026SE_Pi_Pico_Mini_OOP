from led_light import Led_Light
from time import sleep

red_light = Led_Light(3, True, True)

while True:
    red_light.on_for(5)
    sleep(3)