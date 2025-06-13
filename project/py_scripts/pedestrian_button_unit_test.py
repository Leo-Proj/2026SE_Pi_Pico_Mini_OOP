from pedestrian_button import Pedestrian_Button

button = Pedestrian_Button(22, False)

print("Testing button")
while True:
    print(button.button_state(True))