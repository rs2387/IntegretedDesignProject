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

def move_forward(left_speed=68, right_speed=60):
    motor3.Forward(left_speed)
    motor4.Forward(right_speed)


def move_back():
    motor3.Reverse()
    motor4.Reverse()


def stop_motor():
    motor3.off()
    motor4.off()


def adjust_left(speed=75, adjustment=20):
    motor3.Forward(speed=speed - adjustment)
    motor4.Forward(speed=speed)


def adjust_right(speed=70, adjustment=20):
    motor3.Forward(speed=speed)
    motor4.Forward(speed=speed - adjustment)


# --------------------------
# Turning parameters
# --------------------------

CONTINUE_TIME = 1
TURN_SPEED = 60


def right_pivot_90(TURN_SPEED):
    stop_motor()
    sleep(1)
    move_forward()
    sleep(CONTINUE_TIME)
    stop_motor()
    sleep(1)
    condition1 = False
    while True:
        fr = front_right_sensor.value()
        if fr == 1:
            condition1 = True
        motor3.Forward(speed=TURN_SPEED)
        motor4.Reverse(speed=TURN_SPEED)
        ml = middle_left_sensor.value()
        if condition1 == True and ml == 1:
            break
    stop_motor()
    sleep(1)
    


def left_pivot_90(TURN_SPEED):
    stop_motor()
    sleep(1)
    move_forward()
    sleep(CONTINUE_TIME)
    stop_motor()
    sleep(1)
    condition1 = False
    while True:
        fl = front_left_sensor.value()
        if fl == 1:
            condition1 = True
        motor3.Reverse(speed=TURN_SPEED)
        motor4.Forward(speed=TURN_SPEED)
        mr = middle_right_sensor.value()
        if condition1 == True and mr == 1:
            break
    stop_motor()
    sleep(1)

# not useful right now interacts with too many lines
def pivot_180(TURN_SPEED):
    stop_motor()
    sleep(1)
    move_forward()
    sleep(0.5)
    condition1, condition2= False, False
    while True:
        fl = front_left_sensor.value()    
        fr = front_right_sensor.value() 
        if fr == 0:
            condition1 = True
        if condition1 == True and fl == 1:
            condition2 = True
        motor3.Reverse(speed=TURN_SPEED)
        motor4.Forward(speed=TURN_SPEED)
        mr = middle_right_sensor.value()
        if condition2 == True and mr == 1:
            break
    stop_motor()
    sleep(1)
    move_forward()
    sleep(1)

# --------------------------
# main line-following loop
# --------------------------

while True:

    # read all sensors
    ml = middle_left_sensor.value()
    mr = middle_right_sensor.value()
    fl = front_left_sensor.value()
    fr = front_right_sensor.value()

    # Detect pick up first, then turns, then adjusts
    if fr == 1 and mr == 1 and ml == 1 and fl == 1:
        stop_motor()
        sleep(1)
        pivot_180(TURN_SPEED)

    elif fr == 1 and mr == 1 and fl == 0:
        print("Right turn detected")
        right_pivot_90(TURN_SPEED)

    elif fr == 0 and fl == 1 and ml == 1:
        print("Left turn detected")
        left_pivot_90(TURN_SPEED)

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