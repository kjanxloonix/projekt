class Simulator:
    def __init__(self, reference_list, frames=3):
        self.frames_size = frames
        self.frames_list = []
        self.reference_list = reference_list

    def fifo_simulation(self):
        time = 0
        swaps = 0
        not_swaps = 0
        free_frame = 0

        while True:
            if time == len(self.reference_list):
                return time, swaps, not_swaps

            # print('>>'+str(time))

            if len(self.frames_list) != self.frames_size:
                self.frames_list.append(time)

            if (self.reference_list[time] in self.frames_list) is False:
                self.frames_list[free_frame] = self.reference_list[time]
                swaps += 1
                free_frame += 1
                free_frame %= self.frames_size
            else:
                not_swaps += 1

            time += 1
            print(self.frames_list)
