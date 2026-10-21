from movement import right_pivot_90, left_pivot_90

# class for the map with different checkpoints/ states as methods

class Map:
    def __init__(self, checkpoint: str, turning: bool, moving:bool, picked_up_box:bool):
        self.checkpoint = checkpoint
        self.turning = turning
        self.moving = moving
        self.picked_up_box = False
        
    def start(self):
        self.turning = True
        right_pivot_90()


    def right_bays(self, turning:bool, moving:bool):
        self.turning = turning
        self.moving = moving
        self.bays = 2
        self.checkpoint = "right_bay"
        print("Moving to right bay")


    def left_bays(self, turning:bool, moving:bool):
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