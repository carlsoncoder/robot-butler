#!/usr/bin/python

import RPi.GPIO as GPIO #Import the GPIO library as GPIO
import cwiid
import time

#Setup GPIO
GPIO.setmode(GPIO.BCM) # Set the numbers to Broadcom Mode
GPIO.setwarnings(False) # Ignore any errors

#Assign variables to pins
m1a = 17
m1b = 18
m2a = 22
m2b = 23
redLED = 20 #yellow wire
blueLED = 26 #greenwire

button_delay = 0.1

GPIO.setup(m1a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(m1b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(m2a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(m2b,GPIO.OUT) #Set 23 as output (Motor 2 B)

GPIO.setup(redLED, GPIO.OUT) #Set Red LED as output
GPIO.setup(blueLED, GPIO.OUT) #Set Blue LED as output

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
        
        
stop()
GPIO.output(redLED, GPIO.LOW)
GPIO.output(blueLED, GPIO.LOW)
time.sleep(5)

print 'Press 1+2 on your wiimote now!'
GPIO.output(redLED, GPIO.HIGH)
time.sleep(2)

# Try to connect to the Wiimote & quit if not found
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Can't connect to Wiimote"
  quit()

print 'Wiimote connected'
GPIO.output(redLED, GPIO.LOW)
GPIO.output(blueLED, GPIO.HIGH)
wii.rpt_mode = cwiid.RPT_BTN

while True:
  buttons = wii.state['buttons']
  
  # Plus and Minus buttons pressed together simultaneously - rumble and quit
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print 'Closing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
    
  # Forward (Up)
  elif (buttons & cwiid.BTN_UP):
    time.sleep(button_delay)
    forwards()
  
  # Backward (Down) 
  elif (buttons & cwiid.BTN_DOWN):
    time.sleep(button_delay)
    backwards()
  
  # Left (Left)
  elif (buttons & cwiid.BTN_LEFT):
    time.sleep(button_delay)
    left()
   
  # Right (Right)
  elif(buttons & cwiid.BTN_RIGHT):
    time.sleep(button_delay)
    right()
    
  # Right (Right)
  elif(buttons & cwiid.BTN_RIGHT):
    time.sleep(button_delay)
    right()
  
  # A button - Stop all motors
  elif (buttons & cwiid.BTN_A):
    time.sleep(button_delay)
    stop()
  
  # B button - no current action
  elif (buttons & cwiid.BTN_B):
    time.sleep(button_delay)
    print 'Button B pressed - no action'
    
  # 1 button - no current action
  elif (buttons & cwiid.BTN_1):
    time.sleep(button_delay)
    print 'Button 1 pressed - no action'
    
  # 2 button - no current action
  elif (buttons & cwiid.BTN_2):
    time.sleep(button_delay)
    print 'Button 2 pressed - no action'
    
  # Home button - no current action
  elif (buttons & cwiid.BTN_HOME):
    time.sleep(button_delay)
    print 'Button Home pressed - no action'
    
  else:
    stop()