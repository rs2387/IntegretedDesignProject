from motor import Motor
from utime import sleep

motor3 = Motor(dirPin=4, PWMPin=5)
motor4 = Motor(dirPin=6, PWMPin=7)


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


def test():
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


if __name__ == "__main__":
    test()