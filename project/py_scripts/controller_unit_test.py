from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from time import sleep

# led_pedestrian_red = Led_Light(19, True, True)
# led_pedestrian_green = Led_Light(17, False, True)
# led_car_red = Led_Light(3, False, True)
# led_car_amber = led_Light(5, False, True)
# led_car_green = Led_Light(6, False, True)
# pedestrian_button = Pedestrian_Button(22, True)
# buzzer = Audio_Notification(27, True)

red = Led_Light(3,False, True)
amber = Led_Light(5, False, True)
green = Led_Light(6, False, True)
button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

p_red = Led_Light(19, False, True)
p_green = Led_Light(17, False, True)

light = TrafficLightSubsystem(red, amber, green, True)
pedestrian_light = PedestrianSubsystem(p_red, p_green, button, buzzer, True)
controller = Controller(p_red, p_green, red, amber, green, button, buzzer, True)

def Controller_driver():
    print("Testing IDLE state in 2 seconds")
    controller.set_idle_state()
    sleep(2)

    print("Testing CHANGE state in 2 seconds")
    controller.set_change_state()
    sleep(2)

    print("Testing WALK state in 2 seconds")
    controller.set_walk_state()
    sleep(2)

    print("Testing WARNING state in 2 seconds")
    controller.set_warning_state()
    sleep(2)

    print("Testing ERROR state in 2 seconds")
    controller.error_state()
    sleep(2)
