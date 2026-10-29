from movement import (
move_and_adjust,
stop_motor,
pivot_180_left,
pivot_180_right,
left_pivot_90,
right_pivot_90,
move_until_junction,
move_back,
pick_up,
drop_off,
turn_before_pickup
)
from machine import Pin, I2C
from libs.VL53L0X.VL53L0X import VL53L0X
from utime import sleep
from magnet import get_magnet

# Initialise the range sensor once
i2c_bus = I2C(id=0, sda=Pin(8), scl=Pin(9), freq=100000)
vl53l0 = VL53L0X(i2c_bus)

vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[0], 18)
vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[1], 14)

vl53l0.start()
sleep(0.1)


def get_distance():
    """Return the measured distance in mm."""
    distance = vl53l0.read()
    if distance is None:
        get_distance()
        return None

    return int(distance)





def move_till_box(distance_limit=50):
    distance = get_distance()
    while distance is not None and distance >= distance_limit:  #mm, trial and error to find optimal distance
        move_and_adjust(0.1)
        distance = get_distance()
    stop_motor()

# will go through the bays until true is returned, meaning a box isn't is present,
# unless dropping = false (so its picking up), then its the other way round
def detect_box(time, direction, dropping=True):  
    junction_count = 0
    while True:
        junction_count += 1
        # Check the current bay
        move_and_adjust(time)
        distance = get_distance()

        if dropping == True:
            if distance is not None and distance >= 150:  # mm
                stop_motor()
                return junction_count

        else:
            if distance is not None and distance <= 150:
                stop_motor()
                return junction_count

        # box found: turn around
        pivot_180_left(sleeping=True, forward=False, sleeping_time=3)

        move_until_junction()

        if direction == 'left':
        # Turn left into the next bay
            left_pivot_90(continue_time=1.2)

            move_back(left_speed=60, right_speed=60)
            sleep(0.5)
            move_until_junction()
            left_pivot_90(sleeping=True, continue_time=1.2)

        if direction == 'right':
            right_pivot_90(continue_time=1.2)

            move_back(left_speed=60, right_speed=60)
            sleep(0.5)
            move_until_junction()
            right_pivot_90(sleeping=True, continue_time=1.2)


def test():
    sleep(3)
    drop_off()
    # detect_box(2.2, "left")

    detect_box(2.2, 'left', dropping=False)
    move_till_box()
    for i in range(10):
        pole = get_magnet()
        sleep(0.5)
        print(pole)
    pick_up()        
