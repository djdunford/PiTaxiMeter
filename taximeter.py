#!/usr/bin/env python3
#
# Pi Taxi Meter
# uses Pimoroni fourletter-phat
#
# by Darren Dunford

# MIT License
# 
# Copyright (c) 2019 Darren Dunford
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import fourletterphat as flp
import time
import RPi.GPIO as GPIO
import random

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
        flp.clear()
        flp.show()
        time.sleep(1.5)
        flp.set_blink(flp.HT16K33_BLINK_2HZ)
        flp.print_str("HIRE")
        flp.show()
        time.sleep(5)
        flp.set_blink(flp.HT16K33_BLINK_OFF)
        trigger = 0
        
        oldprice = 0
        price = 300
        
        for i in range(oldprice,price):
            flp.clear()
            flp.print_number_str(i)
            flp.show()
        oldprice = price
            
        pricetime = time.time()
        interval = random.randint(10,30)
        while trigger != 1:
        
            # print amount
            flp.clear()
            flp.print_number_str(price)
            flp.show()
            if (int(time.time()*4) % 2) == 1:
                flp.set_decimal(1,True)
            else:
                flp.set_decimal(1,False)
            flp.show()
            
            # randomly between 10 and 30 secs increment by 20p
            if time.time() > pricetime + interval and price < 9980:
                price += 20
                for i in range(oldprice,price):
                    flp.clear()
                    flp.print_number_str(i)
                    flp.show()
                oldprice = price
                interval = random.randint(5,20)
                pricetime = time.time()
        
        trigger = 0
        
        while trigger == 0:
            flp.clear()
            flp.print_str("PAY ")
            flp.show()
            time.sleep(0.5)
            flp.clear()
            flp.print_str(" NOW")
            flp.show()
            time.sleep(0.5)
            flp.clear()
            flp.set_blink(flp.HT16K33_BLINK_2HZ)
            flp.print_number_str(price)
            flp.set_decimal(1,True)
            flp.show()
            time.sleep(6)
            flp.set_blink(flp.HT16K33_BLINK_OFF)
            flp.show()
            time.sleep(1.5)
        
        flp.scroll_print("THANK YOU - PLEASE RIDE AGAIN",0.1)
        time.sleep(1)
        flp.clear()
        flp.show()
        time.sleep(3)
            
        trigger = 0
        
    flp.clear()
    flp.show()
    time.sleep(0.5)