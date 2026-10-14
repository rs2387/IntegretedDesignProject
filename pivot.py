from machine import Pin, PWM
from utime import sleep
from motor import Motor

def left_pivot_90():
    motor3 = Motor(dirPin=4, PWMPin=5)
    motor4 = Motor(dirPin=7, PWMPin=6)

    motor3.Forward(speed=50)
    motor4.Reverse(speed=50)

    sleep(0.1)

    motor3.off()
    motor4.off()

front_left_sensor = Pin(28, Pin.IN)

def sense_to_pivot():
    motor3 = Motor(dirPin=4, PWMPin=5)
    motor4 = Motor(dirPin=7, PWMPin=6)

    motor3.Forward()
    motor4.Forward()

    sleep(0.2)

    motor3.off()
    motor4.off()


if front_left_sensor.value() == 1:
    sense_to_pivot()
    left_pivot_90()