from moving_test import stop_motor, pivot_180, left_pivot_90, right_pivot_90, move_forward, adjust_left, adjust_right

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


CONTINUE_TIME = 1
TURN_SPEED = 60

# --------------------------
# main line-following loop
# --------------------------

if __name__ == "__main__":
    sleep(6)
    count = 0

    while True:
        # read all sensors
        ml = middle_left_sensor.value()
        mr = middle_right_sensor.value()
        fl = front_left_sensor.value()
        fr = front_right_sensor.value()
        if count == 0:
            right_pivot_90(TURN_SPEED, forward=False)
            move_forward()
            sleep(3)
            count = 1

        # Detect pick up first, then turns, then adjusts
        if fr == 1 and mr == 1 and ml == 1 and fl == 1:
            stop_motor()
            sleep(1)
            #reverse_after_pivot()
            #right_pivot_90(TURN_SPEED)
            # not useful right now too complicated
            pivot_180(TURN_SPEED)
            #
            sleep(1)
            left_pivot_90(TURN_SPEED, forward=False)

        elif fr == 1 and mr == 1 and fl == 0:
            #print("Right turn detected")
            right_pivot_90(TURN_SPEED)

        elif fr == 0 and fl == 1 and ml == 1:
            #print("Left turn detected")
            left_pivot_90(TURN_SPEED)

        # Follow the line using the middle sensors
        if ml == 0 and mr == 0:
            #print("Move forward")
            move_forward()

        elif ml == 0 and mr == 1:
            #print("Adjust right")
            adjust_right()

        elif ml == 1 and mr == 0:
            #print("Adjust left")
            adjust_left()

        else:
            pass
            #print("Line lost")

        sleep(0.05)