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