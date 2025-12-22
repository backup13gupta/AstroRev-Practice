#!/usr/bin/python3

# GPIO Control Library
# --------------------
# https://pypi.org/project/rpi-lgpio/
# https://rpi-lgpio.readthedocs.io/en/latest/
# https://rpi-lgpio.readthedocs.io/en/latest/api.html


# *** Import Libraries ***

import RPi.GPIO as GPIO
import time


# *** Set Up Pin Assignments ***

GPIO.setmode ( GPIO.BOARD )  # use header pin numbers, not GPIO numbers

ledPin    = 36  # GPIO 16
buttonPin = 37  # GPIO 26


# *** Event Handler Functions ***

def flipLedState ( pin ):
    ledIsOn = GPIO.input ( ledPin )
    if ( ledIsOn ) :
        GPIO.output ( ledPin, GPIO.LOW  )
    else :
        GPIO.output ( ledPin, GPIO.HIGH )


# *** Set Up Pin Behavior Modes *** 

GPIO.setup ( ledPin,    GPIO.OUT )              # set pin as output
GPIO.setup ( buttonPin, GPIO.IN, GPIO.PUD_UP )  # set pin as input with pull-up resistor


# *** Map Input Pins to Event (Callback) Handlers ***

GPIO.add_event_detect( buttonPin, GPIO.FALLING, callback=flipLedState )  # optionally add debounce time in ms


# *** Drive Pins ***

# Initialize LED...
GPIO.output ( ledPin, GPIO.HIGH )  # turn led on to start

while True:
    pass  # do nothing, but wait for asynchronous button events
