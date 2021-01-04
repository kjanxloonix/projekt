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

        print(" >Symulacja FIFO<")
        while True:
            if time == len(self.reference_list):
                self.frames_list.clear()
                return time, swaps, not_swaps

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

    def lru_simulation(self):
        time = 0
        swaps = 0
        not_swaps = 0
        counters = []

        print(" >Symulacja LRU<")
        while True:
            if time == len(self.reference_list):
                self.frames_list.clear()
                return time, swaps, not_swaps
            if len(self.frames_list) != self.frames_size:
                self.frames_list.append(time)
                counters.append(0)

            if (self.reference_list[time] in self.frames_list) is False:
                index_of_frame = counters.index(min(counters))
                self.frames_list[index_of_frame] = self.reference_list[time]
                counters[index_of_frame] += 1
                swaps += 1
            else:
                for i in range(len(self.frames_list)):
                    if self.reference_list[time] == self.frames_list[i]:
                        counters[i] += 1
                        not_swaps += 1

            print(self.frames_list, counters)
            time += 1
