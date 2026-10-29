from motor import Motor
from utime import sleep
from machine import Pin, ADC
from servos import Servo
from utime import ticks_ms, ticks_diff


hall_effect = ADC(26)
def get_magnet():
    return(hall_effect.read_u16())

# --------------------------
# Declare motors
# --------------------------

motor3 = Motor(dirPin=4, PWMPin=5)
motor4 = Motor(dirPin=7, PWMPin=6)

base_servo = Servo(Pin(15)) # Connected to Servo 1
arm_servo = Servo(Pin(13)) # Connected to Servo 2

# --------------------------
# Assign sensors
# --------------------------

front_left_sensor = Pin(21, Pin.IN)
front_right_sensor = Pin(20, Pin.IN)
middle_left_sensor = Pin(19, Pin.IN)
middle_right_sensor = Pin(18, Pin.IN)

button = Pin(21, Pin.IN)


# --------------------------
# Movement functions
# --------------------------

def move_forward(left_speed=60, right_speed=60):
    motor3.Forward(left_speed)
    motor4.Forward(right_speed+3)


def move_back(left_speed=30, right_speed=30):
    motor3.Reverse(left_speed)
    motor4.Reverse(right_speed)


def stop_motor():
    motor3.off()
    motor4.off()


def adjust_left(speed=73, adjustment=23):
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

def pivot_180_left(turn_speed=TURN_SPEED, sleeping=False, forward=True, sleeping_time=2.0): 
    #stop_motor()
    #sleep(0.5)
    if forward:
        move_forward()
        sleep(0.5)
    condition1, condition2= False, False

    if sleeping == True:
        condition1, condition2 = True, True
        motor3.Reverse(speed=TURN_SPEED)
        motor4.Forward(speed=TURN_SPEED)
        sleep(sleeping_time)
        
        while True:
            motor3.Reverse(speed=TURN_SPEED)
            motor4.Forward(speed=TURN_SPEED)

            mr = middle_right_sensor.value()
            if mr == 1:
                
                break

    elif sleeping == False:        
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


def pivot_180_right(turn_speed=TURN_SPEED, sleeping=False, forward=True, sleeping_time=2.0): 
    #stop_motor()
    #sleep(0.5)
    if forward:
        move_forward()
        sleep(0.5)
    condition1, condition2= False, False

    if sleeping == True:
        condition1, condition2 = True, True
        motor3.Reverse(speed=TURN_SPEED)
        motor4.Forward(speed=TURN_SPEED)
        sleep(sleeping_time)
        
        while True:
            motor3.Reverse(speed=TURN_SPEED)
            motor4.Forward(speed=TURN_SPEED)
            ml = middle_left_sensor.value()
            if ml == 1:
                #sleep(0.05)
                break

    elif sleeping == False:        
        while True:
            fl = front_left_sensor.value()    
            fr = front_right_sensor.value() 
            if fl == 0:
                condition1 = True
            if condition1 == True and fr == 1:
                condition2 = True
            motor3.Reverse(speed=turn_speed)
            motor4.Forward(speed=turn_speed)
            sleep(0.3)
            ml = middle_left_sensor.value()
            if condition2 == True and ml == 1:
                sleep(0.25)
                break
    #stop_motor()
    #sleep(1)


closing_angle = 38
raising_angle = 40
dropping_angle = 22

# make pick_up function gradual rather than instant for smoothness
def pick_up(initial_arm=0, initial_base=270):
    final_arm = initial_arm + closing_angle
    final_base = initial_base - raising_angle
    current_arm = initial_arm
    current_base = initial_base
    while current_arm != final_arm:
        current_arm += 1
        arm_servo.set_angle(current_arm)
        sleep(0.01)
    while current_base != final_base:
        current_base -= 1
        base_servo.set_angle(current_base)
        sleep(0.01)



def drop_off(initial_arm=28, initial_base=240):
    base_servo.set_angle(initial_base+raising_angle)
    sleep(0.5)
    arm_servo.set_angle(initial_arm-closing_angle)

def prep_for_drop():
    base_servo.set_angle(270-dropping_angle)

def move_and_adjust(seconds, right_speed=60, left_speed=60):
    start_time = ticks_ms()

    while ticks_diff(ticks_ms(), start_time) < seconds * 1000:
        ml = middle_left_sensor.value()
        mr = middle_right_sensor.value()
        fl = front_left_sensor.value()
        fr = front_right_sensor.value()

        if [fl, ml, mr, fr] == [0, 0, 0, 0]:
            move_forward(right_speed, left_speed)

        elif [fl, ml, mr, fr] == [0, 0, 1, 0]:
            adjust_right()

        elif [fl, ml, mr, fr] == [0, 1, 0, 0]:
            adjust_left()

        else:
            move_forward()

    stop_motor()

def move_until_junction(right_speed=60, left_speed=60):
    while True:
        ml = middle_left_sensor.value()
        mr = middle_right_sensor.value()
        fl = front_left_sensor.value()
        fr = front_right_sensor.value()
        
        if [fl, ml, mr, fr] == [0, 0, 0, 0]:
            move_forward(right_speed, left_speed)
        
        elif [fl, ml, mr, fr] == [0, 0, 1, 0]:
            adjust_right()
        
        elif [fl, ml, mr, fr] == [0, 1, 0, 0]:
            adjust_left()
        else:
            stop_motor()
            break

def turn_before_pickup():
    motor3.Forward(speed=60)
    motor4.Reverse(speed=60)
    sleep(0.1)
    stop_motor()
