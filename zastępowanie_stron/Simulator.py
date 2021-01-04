class Simulator:
    def __init__(self, frames=3):
        self.frames_size = frames
        self.frames_list = []

    def fifo_simulation(self):
        for i in range(self.frames_size):
            self.frames_list.append(i)
        print(self.frames_list)
