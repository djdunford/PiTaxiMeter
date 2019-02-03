#!/usr/bin/env python3

import fourletterphat
import time
import RPi.GPIO as GPIO

while True:

    # show for hire message
    fourletterphat.clear()
    fourletterphat.scroll_print("UBER DAVE  -  FOR HIRE", 0.2)
    # button 2 held down should initiate a shutdown
    
    # button 1 starts the hiring sequence
    
