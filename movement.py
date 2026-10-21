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

def move_forward(left_speed=62, right_speed=60):
    motor3.Forward(left_speed)
    motor4.Forward(right_speed)


def move_back(left_speed=32, right_speed=30):
    motor3.Reverse(left_speed)
    motor4.Reverse(right_speed)


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

CONTINUE_TIME = 1.05
TURN_SPEED = 60


def right_pivot_90(turn_speed=TURN_SPEED, forward=True, continue_time=CONTINUE_TIME,  sleeping = False):
    #stop_motor()
    #sleep(1)
    if forward:
        move_forward()
        sleep(continue_time)
        #stop_motor()
        #sleep(1)
    condition1 = False

    if sleeping == True:
        condition1 = True
        motor4.Reverse(speed=turn_speed)
        motor3.Forward(speed=turn_speed)
        sleep(1)

    while True:
        fr = front_right_sensor.value()
        if fr == 1:
            condition1 = True
        motor3.Forward(speed=turn_speed)
        motor4.Reverse(speed=turn_speed)
        ml = middle_left_sensor.value()
        if condition1 == True and ml == 1:
            sleep(0.05)
            break
    #stop_motor()
    #sleep(1)
    


def left_pivot_90(turn_speed=TURN_SPEED, forward=True, continue_time=CONTINUE_TIME, sleeping = False):
    #stop_motor()
    #sleep(1)
    if forward:
        move_forward()
        sleep(continue_time)
        #stop_motor()
        #sleep(1)
    condition1 = False

    if sleeping == True:
        condition1 = True
        motor3.Reverse(speed=turn_speed)
        motor4.Forward(speed=turn_speed)
        sleep(1)


    while True:
        fl = front_left_sensor.value()
        if fl == 1:
            condition1 = True
        motor3.Reverse(speed=turn_speed)
        motor4.Forward(speed=turn_speed)
        mr = middle_right_sensor.value()
        if condition1 == True and mr == 1:
            #sleep(0.05)
            break
    #stop_motor()
    #sleep(1)


def reverse_after_pivot():
    #stop_motor()
    #sleep(1)
    move_back()
    sleep(1)
    while True:
        move_back()
        ml = middle_left_sensor.value()
        mr = middle_right_sensor.value()
        fl = front_left_sensor.value()
        fr = front_right_sensor.value()
        if mr == 1 and ml == 1 and fr ==1 and fl ==1:
            break
    #stop_motor()
    #sleep(1)
    move_forward()
    sleep(1)
    #stop_motor()
    #sleep(1)

# not useful right now interacts with too many lines
def pivot_180(turn_speed=TURN_SPEED, sleeping = False):
    #stop_motor()
    #sleep(0.5)
    move_forward()
    sleep(0.5)
    condition1, condition2= False, False

    #beginings of making 1 180 function
    #if sleeping == True:
    #    condition1, condition2 = True, True

    while True:
        fl = front_left_sensor.value()    
        fr = front_right_sensor.value() 
        if fr == 0:
            condition1 = True
        if condition1 == True and fl == 1:
            condition2 = True
        motor3.Reverse(speed=turn_speed)
        motor4.Forward(speed=turn_speed)
        sleep(0.3)
        mr = middle_right_sensor.value()
        if condition2 == True and mr == 1:
            sleep(0.25)
            break
    #stop_motor()
    #sleep(1)

def reverse_180():
    #stop_motor()
    #sleep(1)
    #reverse_after_pivot()
    #right_pivot_90(TURN_SPEED)
    # not useful right now too complicated
    pivot_180(TURN_SPEED)
    
    #sleep(1)
    left_pivot_90(TURN_SPEED, forward=False)

def bay_left_180(TURN_SPEED):
    #stop_motor()
    #sleep(1)
   
    motor3.Reverse(speed=TURN_SPEED)
    motor4.Forward(speed=TURN_SPEED)
    sleep(2)
        
    while True:
        motor3.Reverse(speed=TURN_SPEED)
        motor4.Forward(speed=TURN_SPEED)
        mr = middle_right_sensor.value()
        if mr == 1:
            #sleep(0.05)
            break
    #stop_motor()
    #sleep(1)
