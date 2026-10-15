from motor import Motor
from utime import sleep
from machine import Pin

# --------------------------
# Declare motors
# --------------------------

motor3 = Motor(dirPin=4, PWMPin=5)
motor4 = Motor(dirPin=7, PWMPin=6)


# --------------------------
# Assign sensors
# --------------------------

front_left_sensor = Pin(28, Pin.IN)
front_right_sensor = Pin(27, Pin.IN)
middle_left_sensor = Pin(26, Pin.IN)    
middle_right_sensor = Pin(22, Pin.IN)  

button = Pin(21, Pin.IN)


# --------------------------
# Movement functions
# --------------------------

def move_forward():
    motor3.Forward(speed=40)
    motor4.Forward(speed=40)


def move_back():
    motor3.Reverse()
    motor4.Reverse()


def stop_motor():
    motor3.off()
    motor4.off()


def adjust_left(speed=40, adjustment=10):
    motor3.Forward(speed=speed - adjustment)
    motor4.Forward(speed=speed)


def adjust_right(speed=40, adjustment=10):
    motor3.Forward(speed=speed)
    motor4.Forward(speed=speed - adjustment)


# --------------------------
# Turning parameters
# --------------------------

turntime = 0.5
continuetime = 0.5
turnspeed = 50


def left_pivot_90(turntime, turnspeed):
    motor3.Forward(speed=turnspeed)
    motor4.Reverse(speed=turnspeed)

    sleep(turntime)
    stop_motor()


def right_pivot_90(turntime, turnspeed):
    motor4.Forward(speed=turnspeed)
    motor3.Reverse(speed=turnspeed)

    sleep(turntime)
    stop_motor()


def sense_to_pivot(continuetime):
    move_forward()
    sleep(continuetime)
    stop_motor()


# --------------------------
# main line-following loop
# --------------------------

while True:

    # read all sensors
    ml = middle_left_sensor.value()
    mr = middle_right_sensor.value()
    fl = front_left_sensor.value()
    fr = front_right_sensor.value()

    # Detect turns first
    # if fr == 1 and fl == 0:
    #     print("Right turn detected")
    #     sense_to_pivot(continuetime)
    #     right_pivot_90(turntime, turnspeed)

    # elif fr == 0 and fl == 1:
    #     print("Left turn detected")
    #     sense_to_pivot(continuetime)
    #     left_pivot_90(turntime, turnspeed)

    # Follow the line using the middle sensors
    if ml == 0 and mr == 0:
        print("Move forward")
        move_forward()

    elif ml == 0 and mr == 1:
        print("Adjust right")
        adjust_right()

    elif ml == 1 and mr == 0:
        print("Adjust left")
        adjust_left()

    else:
        print("Line lost")

    sleep(0.05)