from pedestrian_button import Pedestrian_Button

button = Pedestrian_Button(22, False)

while True:
    print(button.button_state())
    sleep(0.5)