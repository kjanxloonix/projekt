class Simulator:
    def __init__(self, generator, algorithm=''):
        self.worklist = []
        self.gen = generator
        self.alg = algorithm

    def fcfs_simulation(self):
        # TODO symulacja
        time = 0
        while True:
            for i in self.gen.process_list:
                if i.arrive_t == time:
                    self.worklist.append(i)
                    print(self.worklist)
                    break
            for i in self.worklist:
                print(i.arrive_t)
                exit()

            time += 1
