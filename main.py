from movement import (
    stop_motor,
    left_pivot_90,
    right_pivot_90,
    move_forward,
    adjust_left,
    adjust_right,
    pivot_180_left,
    pivot_180_right,
    pick_up,
    drop_off,
    move_and_adjust,
    move_back,
    turn_before_pickup,
    prep_for_drop
)
from magnet import get_magnet
from utime import sleep
from machine import Pin
from motor import Motor
from range import get_distance, move_till_box, detect_box
from led import led

motor3 = Motor(dirPin=4, PWMPin=5)
motor4 = Motor(dirPin=7, PWMPin=6)


# --------------------------
# Assign sensors
# --------------------------

front_left_sensor = Pin(21, Pin.IN)
front_right_sensor = Pin(20, Pin.IN)
middle_left_sensor = Pin(19, Pin.IN)
middle_right_sensor = Pin(18, Pin.IN)


amber_led = led(11)

button = Pin(21, Pin.IN)

SKIP_TIME = 0.7  # The time it sleeps whilst moving over a junction it wants to skip
CONTINUE_TIME = 1.05  # The time it creeps before pivoting 90 degrees
TURN_SPEED = 60  # The speed at which the motors move during a turn

# --------------------------
# main line-following loop
# --------------------------


def get_sensors():
        ml = middle_left_sensor.value()
        mr = middle_right_sensor.value()
        fl = front_left_sensor.value()
        fr = front_right_sensor.value()
        return fr, mr, ml, fl
         

# defines route from left bays to bottom loading rack

def left_bay_to_bottom_rack(count=4, bay_number=1):

    count = count
    
    while True:
        fr, mr, ml, fl = get_sensors()

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

    # it will turn left at the next junction and will be out of bay 1/2
            if count == 4:
                left_pivot_90(TURN_SPEED, continue_time=1.1)
                if bay_number ==2:
                    count += 1 # skip the skipping bay 2 elif
                count +=1

    #skipping bay 2
            elif count == 5:
                move_and_adjust(SKIP_TIME)
                count += 1

    #turn into bottom loading rack, drop off block, then turn around
            elif count == 6:
                rack_number = detect_box(direction='left', time=2)
                prep_for_drop()
                move_and_adjust(1)
                drop_off()
                move_back(left_speed=70, right_speed=70)
                sleep(1)
                pivot_180_left(TURN_SPEED, sleeping=True, forward=False)
                # now need to ignore rack_number junctions for the way back
                count += 1

    #exit loading rack
            elif count == 7:
                right_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                # at this point we have rack_number of junctions in front of us to skip
                move_and_adjust(4*SKIP_TIME*rack_number)
                count += 1

    #skip next 2 bays
            elif count == 8:
                move_and_adjust(SKIP_TIME)
                count += 1

            elif count == 9:
                move_and_adjust(SKIP_TIME)
                count += 1

    #right turn
            elif count == 10:
                right_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                count += 1

            elif count == 11:
                move_and_adjust(SKIP_TIME)
                count += 1

    #stop in centre
            elif count == 12:
                right_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                stop_motor()
                sleep(10)
                break

        sleep(0.05)
            
# defines route from left bays to top loading rack 

def left_bay_to_top_rack(count=4, bay_number=1):

    count = count

    while True:
        fr, mr, ml, fl = get_sensors()

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

    # it will turn right at the next junction and will be out of bay 1
            if count == 4:
                right_pivot_90(TURN_SPEED, continue_time=1.1)
                if bay_number == 2:
                    count += 0.5
                elif bay_number ==1:
                    count +=1

    # if coming out of bay 2, then need to skip bay 1 entrance
            if count == 4.5:
                move_and_adjust(SKIP_TIME)
                count += 0.5

    # turning right at the corner back the way we came
            elif count == 5:
                right_pivot_90(TURN_SPEED)
                count += 1

    # junction at the start, skip the first line
            elif count == 6:
                move_and_adjust(SKIP_TIME)
                count += 1

    # turns right to face towards the ramp
            elif count == 7:
                right_pivot_90(TURN_SPEED)
                count += 1

    # skip this junction and continue moving towards the ramp
            elif count == 8:
                move_and_adjust(SKIP_TIME)
                count += 1

    # ramp is detected
            elif count == 9:
                #move up increasing speed by a good amount to get up the ramp
                move_and_adjust(3, right_speed=100, left_speed=100)
                count += 1

    #turn into top loading rack, drop off block, then turn around
            elif count == 10:
                right_pivot_90(TURN_SPEED, sleeping=True)
                move_and_adjust(3.5)
                drop_off()
                move_back(left_speed=70, right_speed=70)
                sleep(1)
                # sleep for longer to ensure it doesnt interfere with other lines
                pivot_180_left(TURN_SPEED, sleeping=True, forward=False, sleeping_time=2.5)
                count += 1

    #exit top loading rack
            elif count == 11:
                left_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                count += 1
                # starts to go down the ramp

    # end of ramp detected
            elif count == 12:
                # make it slow down at the end of the ramp
                move_and_adjust(1, right_speed=40, left_speed=40)
                count += 1

    # start of initial start area detected
            elif count == 13:
                move_and_adjust(SKIP_TIME)
                count += 1

    # stop in centre
            elif count == 14:
                stop_motor()
                sleep(1)
                left_pivot_90(TURN_SPEED, sleeping=True)
                left_pivot_90(TURN_SPEED, forward=False)
                stop_motor()
                sleep(10)
                break

        sleep(0.05)
            



if __name__ == "__main__":


    sleep(8)
    count = 0

    while True:
        amber_led.flash()
        fr, mr, ml, fl = get_sensors()

        if count == 0:
            drop_off()
            right_pivot_90(TURN_SPEED, forward=False)
            move_and_adjust(1.5)
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
                #left_pivot_90(TURN_SPEED, continue_time=CONTINUE_TIME)
                bay_number = detect_box(time=1, dropping=False, direction="left")

                count += 1

# pick up box and reverse 180 
            elif count == 3:
                move_till_box(70)
                sleep(1)
                turn_before_pickup()
                sleep(1)
                move_till_box()
                sleep(1)
                pole = get_magnet()
                sleep(1)
                pick_up()
                pivot_180_left(sleeping=True)

                count += 1

                 

# will move forward normally and adjust to line until it detects junction

            if count == 4:
                if pole == "south":
                    left_bay_to_bottom_rack(count = count, bay_number=bay_number)
                    # takes us back to the centre so we can start again
                    count = 0 # reset
                elif pole == "north":
                    left_bay_to_top_rack(count = count, bay_number=bay_number)
                    # takes us back to the centre so we can start again
                    count = 0 # reset


        sleep(0.05)
    amber_led.off()