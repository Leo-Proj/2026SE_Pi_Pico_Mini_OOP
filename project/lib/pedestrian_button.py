from machine import Pin
from time import ticks_ms, ticks_diff

class Pedestrian_Button(Pin):
    '''
    A class which gives a button the functionality of a pedestrian button

    arguements:
        pin (int): GPIO pin number for the button

    examples:
        button = pedestrian_button (22) # connected to pin 22
    '''

    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_press = 0
        self.__pedestrian_waiting = False
        self.button_state

    @property
    '''
    Get the state of the button, not whether the button is being pressed or not pressed, but if the button has been pressed
    '''
    def button_state(self):
        if self.__debug:
            print(f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}")
        return self.__pedestrian_waiting
    
    @button_state.setter
    '''
    Resets the pedestrian_waiting 
    '''
    def button_state(self, value):
        self.__pedestrian_waiting = value
        if self.__debug:
            print(f"Button state on Pin {self.__pin} set to {value}")

    class Pedestrian_Button(Pin):
    '''
    Records the state change without interupting current processes
    '''
        def __init__(self, pin, debug):
            ...
            self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    def callback(self, pin):
        current_time = time.ticks_ms()
        if (time.ticks_diff(current_time, self.__last_pressed) > 200):
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")