from moving import turn_right, turn_left

# class for the map with different checkpoints/ states as methods

class Map:
    def __init__(self, checkpoint, turning, moving):
        self.checkpoint = checkpoint
        self.turning = turning
        self.moving = moving
        
    def start(self):
        self.turning = True
        turn_right()


    def right_bay(self, turning:bool, moving:bool):
        self.turning = turning
        self.moving = moving
        self.bays = 2
        self.checkpoint = "right_bay"
        print("Moving to right bay")


    def left_bay(self, turning:bool, moving:bool):
        self.turning = turning
        self.moving = moving
        self.bays = 2
        self.checkpoint = "left_bay"
        print("Moving to left bay")


    def rack_A_bottom(self, turning:bool, moving:bool):
        self.turning = turning
        self.moving = moving
        self.racks = 6
        self.checkpoint = "rack_A_bottom"
        print("Moving to rack A bottom")


    def rack_A_top(self, turning:bool, moving:bool):
        self.turning = turning
        self.moving = moving
        self.racks = 6
        self.checkpoint = "rack_A_top"
        print("Moving to rack A top")

    def rack_B_bottom(self, turning:bool, moving:bool):
        self.turning = turning
        self.moving = moving
        self.racks = 6
        self.checkpoint = "rack_B_bottom"
        print("Moving to rack B bottom")


    def rack_B_top(self, turning:bool, moving:bool):
        self.turning = turning
        self.moving = moving
        self.racks = 6
        self.checkpoint = "rack_B_top"
        print("Moving to rack B top")