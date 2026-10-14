from machine import Pin, PWM
from utime import sleep
from motor import Motor

##### In the future these functions should possibly use the movement functions definded in moving
##### I haven't used them here because I wanted to set the speeds myself

def left_pivot_90(turntime, turnspeed):
    motor3 = Motor(dirPin=4, PWMPin=5)
    motor4 = Motor(dirPin=7, PWMPin=6)

    motor3.Forward(speed=turnspeed)
    motor4.Reverse(speed=turnspeed)

    sleep(turntime)

    motor3.off()
    motor4.off()

def right_pivot_90(turntime, turnspeed):
    #flipped motor 3 and 4 for simple change
    motor4 = Motor(dirPin=4, PWMPin=5)
    motor3 = Motor(dirPin=7, PWMPin=6)

    motor3.Forward(speed=turnspeed)
    motor4.Reverse(speed=turnspeed)

    sleep(turntime)

    motor3.off()
    motor4.off()

#time after sensing line where robot continues advancing so that pivot point is directly above junction
#trial and error neccessary to find correct value of 'time'
def sense_to_pivot(continuetime):
    motor3 = Motor(dirPin=4, PWMPin=5)
    motor4 = Motor(dirPin=7, PWMPin=6)

    motor3.Forward()
    motor4.Forward()

    sleep(continuetime)

    motor3.off()
    motor4.off()

front_left_sensor = Pin(28, Pin.IN)
front_right_sensor = Pin(27, Pin.IN)

#variables that we'll find through trial and error
turntime = 0.5
continuetime = 0.5
turnspeed = 50


#Wont be as simple as an if statement but use this to test
if front_left_sensor.value() == 1:
    sense_to_pivot(continuetime)
    left_pivot_90(turntime, turnspeed)

if front_right_sensor.value() == 1:
    sense_to_pivot(continuetime)
    right_pivot_90(turntime, turnspeed)
