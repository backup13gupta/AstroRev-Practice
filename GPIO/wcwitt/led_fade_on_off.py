#!/usr/bin/python3

# GPIO Control Library
# --------------------
# https://pypi.org/project/rpi-lgpio/
# https://rpi-lgpio.readthedocs.io/en/latest/
# https://rpi-lgpio.readthedocs.io/en/latest/api.html


# *** Import libraries ***

import RPi.GPIO as GPIO
import time


# *** Set Up Pin Assignments ***

GPIO.setmode ( GPIO.BOARD )  # use header pin numbers, not GPIO numbers

ledPin = 32  # GPIO 12 / PWM0


# *** Set Up Pin Behavior Modes *** 

GPIO.setup ( ledPin, GPIO.OUT )  # set pin as output


# *** Drive Pins ***

ledPwm = GPIO.PWM( ledPin, 50 )  # set up pwm frequency(Hz) and get pwm object
ledPwm.start ( 0 )               # start pwm action at 0% duty cycle

while True:
    for dutyCycle in range (   0, 101,  5 ):
        ledPwm.ChangeDutyCycle ( dutyCycle )
        time.sleep ( 0.05 )
    for dutyCycle in range ( 100,  -1, -5 ):
        ledPwm.ChangeDutyCycle ( dutyCycle )
        time.sleep ( 0.05 )