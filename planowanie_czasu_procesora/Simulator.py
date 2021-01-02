class Simulator:
    def __init__(self, generator):
        self.worklist = []
        self.calculated_processes = []
        self.executing_time = 0
        self.gen = generator

    def fcfs_simulation(self):
        # TODO symulacja
        time = 0
        while True:
            print("---", self.executing_time)

            for i in self.gen.process_list:
                if i.arrive_t == time:
                    self.worklist.append(i)

            if self.executing_time == 0:
                self.executing_time = self.worklist[0].exec_t

            for i in self.worklist:
                print(i.arrive_t, i.exec_t, i.end_t)

            time += 1
            self.worklist[0].exec_t -= 1

            if self.worklist[0].exec_t == 0:
                self.worklist[0].exec_t = self.executing_time
                self.executing_time = 0
                self.worklist[0].end_t = time
                self.calculated_processes.append(self.worklist[0])
                self.worklist.pop(0)
            for i in self.calculated_processes:
                print("||", i.arrive_t, i.exec_t, i.end_t)
            print(time)
            if len(self.gen.process_list) == len(self.calculated_processes):
                break
