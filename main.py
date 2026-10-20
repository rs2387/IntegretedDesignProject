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
from motor import Motor

motor3 = Motor(dirPin=4, PWMPin=5)
motor4 = Motor(dirPin=7, PWMPin=6)

# Functions are in wierd files but dont want to cause merge conflict

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

    def bay_left_90(TURN_SPEED, forward=True):
        stop_motor()
        sleep(1)
        if forward:
            move_forward()
            sleep(CONTINUE_TIME)
            stop_motor()
            sleep(1)

 
        motor3.Reverse(speed=TURN_SPEED)
        motor4.Forward(speed=TURN_SPEED)
        sleep(1)

        while True:
            motor3.Reverse(speed=TURN_SPEED)
            motor4.Forward(speed=TURN_SPEED)
            mr = middle_right_sensor.value()
            if mr == 1:
                #sleep(0.05)
                break
        stop_motor()
        sleep(1)

    def bay_left_180(TURN_SPEED):
        stop_motor()
        sleep(1)
   
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
        stop_motor()
        sleep(1)
         


    sleep(10)
    count = 0

    while True:
        fr, mr, ml, fl = get_sensors()

        if count == 0:
            right_pivot_90(TURN_SPEED, forward=False)
            move_forward()
            sleep(1.5)
            count = 1
            continue

                 # Follow the line using the middle sensors
        if [fl, ml, mr, fr] == [0, 0, 0, 0]:
            #print("Move forward")
            move_forward()

        elif [fl, ml, mr, fr] == [0, 0, 1, 0]:
            #print("Adjust right")
            adjust_right()

        elif [fl, ml, mr, fr] == [0, 1, 0, 0]:
                #print("Adjust left")
            adjust_left()

        elif [fl, ml, mr, fr] == [0, 1, 1, 0]:
            move_forward()

        else:
            print("junction detected")

#first corner
            if count == 1:
                left_pivot_90(TURN_SPEED)
                count += 1

#begining of bay 1
            elif count == 2:
                left_pivot_90(TURN_SPEED)
                count += 1

# turning in bay 1
            elif count == 3:
                reverse_180()
                move_forward()
                sleep(0.5)
                left_pivot_90(TURN_SPEED, continue_time=0.6)
                count += 1
#skipping bay 2
            elif count == 4:
                move_forward()
                sleep(1)
                count += 1

#turn into loading bay, go forwards, then turn around
            elif count == 5:
                bay_left_90(TURN_SPEED)
                move_forward()
                sleep(2)
                stop_motor()
                sleep(1)
                bay_left_180(TURN_SPEED)
                count += 1
#exit loading bay
            elif count == 6:
                right_pivot_90(TURN_SPEED)
                count += 1

#skip next 2 bays
            elif count == 7:
                move_forward()
                sleep(1)
                count += 1

            elif count == 8:
                move_forward()
                sleep(1)
                count += 1

#right turn
            elif count == 9:
                right_pivot_90(TURN_SPEED)
                count += 1

            elif count == 10:
                move_forward()
                sleep(1)
                count += 1

#stop in centre
            elif count == 11:
                right_pivot_90(TURN_SPEED)
                stop_motor()
                sleep(10)
                break

        sleep(0.05)
            


            
