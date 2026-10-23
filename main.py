from movement import (
    stop_motor,
    left_pivot_90,
    right_pivot_90,
    move_forward,
    adjust_left,
    adjust_right,
    reverse_180,
    pivot_180,
    towards_box_magnet,
    pick_up,
    drop_off
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

front_left_sensor = Pin(21, Pin.IN)
front_right_sensor = Pin(20, Pin.IN)
middle_left_sensor = Pin(19, Pin.IN)
middle_right_sensor = Pin(18, Pin.IN)

button = Pin(21, Pin.IN)

SKIP_TIME = 0.7  # The time it sleeps whilst moving over a junction it wants to skip
CONTINUE_TIME = 1.05  # The time it creeps before pivoting 90 degrees
TURN_SPEED = 60  # The speed at which the motors move during a turn

# --------------------------
# main line-following loop
# --------------------------

if __name__ == "__main__":

    def get_sensors():
        ml = middle_left_sensor.value()
        mr = middle_right_sensor.value()
        fl = front_left_sensor.value()
        fr = front_right_sensor.value()
        return fr, mr, ml, fl
         

    sleep(5)
    count = 0

    while True:
        fr, mr, ml, fl = get_sensors()

        if count == 0:
            drop_off()
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
            #print("junction detected")

#first corner
            if count == 1:
                left_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                count += 1

#begining of bay 1
            elif count == 2:
                left_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                count += 1

# turning out of bay 1
            elif count == 3:
                pick_up()
                reverse_180()
                move_forward()
                sleep(0.5)
                left_pivot_90(TURN_SPEED, continue_time=0.6)
                count += 1

#skipping bay 2
            elif count == 4:
                move_forward()
                sleep(SKIP_TIME)
                count += 1

#turn into loading bay, pick up block, then turn around
            elif count == 5:
                left_pivot_90(TURN_SPEED, sleeping=True)
                move_forward()
                sleep(2)
                drop_off()
 
                pivot_180(TURN_SPEED, sleeping=True)
                count += 1

#exit loading bay
            elif count == 6:
                right_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                count += 1

#skip next 2 bays
            elif count == 7:
                move_forward()
                sleep(SKIP_TIME)
                count += 1

            elif count == 8:
                move_forward()
                sleep(SKIP_TIME)
                count += 1

#right turn
            elif count == 9:
                right_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                count += 1

            elif count == 10:
                move_forward()
                sleep(SKIP_TIME)
                count += 1

#stop in centre
            elif count == 11:
                right_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                stop_motor()
                sleep(10)
                break

        sleep(0.05)
            


            
