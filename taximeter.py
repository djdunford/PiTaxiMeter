#!/usr/bin/env python3

import fourletterphat as flp
import time
import RPi.GPIO as GPIO

# clear trigger
trigger = 0

# Set the GPIO PIN naming mode
GPIO.setmode(GPIO.BCM)

# Suppress warnings for GPIO usage clashes
GPIO.setwarnings(False)

# create array for BCM lines corresponding to buttons
# format is [ BCM line , button_number ]
buttons = [[15,1],[24,2]]

# define button press callback function
def button_press_callback(channel):

    # access global variables
    global trigger

    # set sequence based on button pressed
    for button in buttons:    
        if channel == button[0]:    
            if GPIO.input(button[0]) == False:
                trigger = button[1]            
                
    return

# set each button as an input pin, with pullup,
# and set an event handler based on falling edge
# detection with debounce time
for button in buttons:
    GPIO.setup(button[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(button[0], GPIO.FALLING, callback=button_press_callback, bouncetime=50)

# loop forever
while True:
    flp.clear()
    flp.scroll_print("UBER DAVE FOR HIRE", 0.2)

    if trigger == 1:
        fourlettetphat.clear()
        flp.scroll_print("HIRED",0.2)