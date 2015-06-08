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


#Make both motors go forwards
def forwards():
        GPIO.output(m1a,1) # Motor 1 Forwards turn on
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,1) # Motor 2 Forwards turn on
        GPIO.output(m2b,0) # Motor 2 Backwards turn off

#make both motors go backwards
def backwards():
        GPIO.output(m1a,0) # Motor 1 Forwards turn off
        GPIO.output(m1b,1) # Motor 1 Backwards turn on
        GPIO.output(m2a,0) # Motor 2 Forwards turn off
        GPIO.output(m2b,1) # Motor 2 Backwards turn on
        
#Make motors turn fwd, bak      
def right():
        GPIO.output(m1a,1) # Motor 1 Forwards turn on
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,0) # Motor 2 Forwards turn off
        GPIO.output(m2b,1) # Motor 2 Backwards turn on
        #Make both motors go forwards

#Make motors turn fwd, bak          
def left():
        GPIO.output(m1a,0) # Motor 1 Forwards turn off
        GPIO.output(m1b,1) # Motor 1 Backwards turn on
        GPIO.output(m2a,1) # Motor 2 Forwards turn on
        GPIO.output(m2b,0) # Motor 2 Backwards turn off
        
##All off
def stop():
        GPIO.output(m1a,0) # Motor 1 Forwards turn off
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,0) # Motor 2 Forwards turn off
        GPIO.output(m2b,0) # Motor 2 Backwards turn off
        
        
#Forever
while True:

    #Turn motors Right
    print "Right"
    right()
    #sleep for 2 seconds
    sleep(2)
    
    #Turn motors forward
    print "forwards"
    forwards()
    #sleep for 2 seconds
    sleep(2)
    
    #Turn motors backward
    print "backwards"
    backwards()
    #sleep for 2 seconds
    sleep(2)
    
    #Turn motors left
    print "Left"
    left()
    #sleep for 2 seconds
    sleep(2)
    
    #Stop
    print "stop"
    stop()
    #sleep 1 second
    sleep(1)