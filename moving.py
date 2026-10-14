from motor import Motor
from utime import sleep

# declare the motors
motor3 = Motor(dirPin=4, PWMPin=5)
motor4 = Motor(dirPin=7, PWMPin=6)

#--------------------------
# Functions to move in all directions and to test motor
#--------------------------

def move_right():
    motor3.Forward()
    motor4.Reverse()


def move_left():
    motor3.Reverse()
    motor4.Forward()

def move_forward():
    motor3.Forward()
    motor4.Forward()



def move_back():
    motor3.Reverse()
    motor4.Reverse()

def stop_motor():
    motor3.off()
    motor4.off()


def test_motors():
    while True:
        print("forward")
        move_forward()
        sleep(2)
        print("back")
        move_back()
        sleep(2)
        print("right")
        move_right()
        sleep(2)
        print("left")
        move_left()
        sleep(2)

#--------------------
# Functions to actually turn left or right
#--------------------

# some more logic for actually turning about a pivot
def turn_right():
    move_right()

# some more logic for actually turning about a pivot
def turn_left():
    move_left()





# takes an input true or false from line sensor
# main will call everything
# moving will define all movement
# need a mapping state file as well

# 2 sensors in the middle
# middle_right_sensor, middle_left_sensor

# 2 sensor at the front
# front_right_sensor, front_left_sensor

# set test values
middle_right_sensor = True
middle_left_sensor = True
front_right_sensor = True
front_left_sensor = True

# state variables to partition moving and turning states
moving = True
turning = False


# the two middle sensors are just for moving in a straight line and making sure we are following the tape
# the tape thickness is rouhgly 25 mm
while moving and not turning:
    if middle_left_sensor and middle_right_sensor:
        print("move straight")
        move_forward()
    elif middle_left_sensor and not middle_right_sensor:
        print("adjust to the left")
        move_left()
    elif middle_right_sensor and not middle_left_sensor:
        print("adjust to the left")
        move_left()


if front_right_sensor and not front_left_sensor:
    turning = True
    turn_right()

if front_right_sensor and not front_left_sensor:
    turning = True
    turn_left()
