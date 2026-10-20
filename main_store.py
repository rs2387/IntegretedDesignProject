from moving_test import (
    stop_motor,
    pivot_180,
    left_pivot_90,
    right_pivot_90,
    move_forward,
    adjust_left,
    adjust_right,
)
from utime import sleep
from machine import Pin

# Motors are already declared in moving_test.py

# --------------------------
# Assign sensors
# --------------------------

front_left_sensor = Pin(28, Pin.IN)
front_right_sensor = Pin(27, Pin.IN)
middle_left_sensor = Pin(26, Pin.IN)
middle_right_sensor = Pin(22, Pin.IN)

button = Pin(21, Pin.IN)

CONTINUE_TIME = 1.1
TURN_SPEED = 60

# --------------------------
# main line-following loop
# --------------------------

if __name__ == "__main__":

    def reverse_180():
        stop_motor()
        sleep(1)
        #reverse_after_pivot()
        #right_pivot_90(TURN_SPEED)
        # not useful right now too complicated
        pivot_180(TURN_SPEED)
        #
        sleep(1)
        left_pivot_90(TURN_SPEED, forward=False)

    def get_sensors():
        ml = middle_left_sensor.value()
        mr = middle_right_sensor.value()
        fl = front_left_sensor.value()
        fr = front_right_sensor.value()
        return fr, mr, ml, fl

    sleep(10)
    count = 0

    try:
        while True:
            # read all sensors

            fr, mr, ml, fl = get_sensors()

            if count == 0:
                right_pivot_90(TURN_SPEED, forward=False)
                move_forward()
                sleep(1.5)
                count = 1
                continue

            # Detect pick up first, then turns, then adjusts
            if fr == 1 and mr == 1 and ml == 1 and fl == 1:
                stop_motor()
                reverse_180()
                continue

            elif fr == 1 and mr == 1 and fl == 0:
                move_forward()
                sleep(0.05) # a sleep to make sure its a junction left not a bay
                fr, mr, ml, fl = get_sensors()
                if fr == 1 and mr == 1 and fl == 0:
                    #print("Right turn detected")
                    right_pivot_90(TURN_SPEED, forward=True)
                elif fr == 1 and mr == 1 and ml == 1 and fl == 1:
                    reverse_180()
                continue

            elif fr == 0 and fl == 1 and ml == 1:
                move_forward()
                sleep(0.05) # a sleep to make sure its a junction left not a bay
                fr, mr, ml, fl = get_sensors()
                if fr == 0 and fl == 1 and ml == 1:
                    #print("left turn detected")
                    left_pivot_90(TURN_SPEED, forward=True)
                elif fr == 1 and mr == 1 and ml == 1 and fl == 1:
                    reverse_180()
                continue

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

            elif mr == 1 and ml == 1:
                move_forward()

            else:
                pass
                #print("Line lost")

            sleep(0.08)

    finally:
        stop_motor()