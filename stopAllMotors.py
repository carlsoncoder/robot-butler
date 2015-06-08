#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO #Import the GPIO library as GPIO

#Setup GPIO
GPIO.setmode(GPIO.BCM) # Set the numbers to Broadcom Mode
GPIO.setwarnings(False) # Ignore any errors

#Assign variables to pins
m1a = 17
m1b = 18
m2a = 22
m2b = 23

GPIO.setup(m1a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(m1b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(m2a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(m2b,GPIO.OUT) #Set 23 as output (Motor 2 B)

#Turn all motors off
GPIO.output(m1a,0) # Motor 1 Forwards turn off
GPIO.output(m1b,0) # Motor 1 Backwards turn off
GPIO.output(m2a,0) # Motor 2 Forwards turn off
GPIO.output(m2b,0) # Motor 2 Backwards turn off