import statistics

class Simulator:
    def __init__(self, generator):
        self.worklist = []
        self.calculated_processes = []
        self.waiting_times = []
        self.executing_time = 0
        self.gen = generator

    def fcfs_simulation(self):
        if len(self.gen.process_list) == 0:
            return "Błąd!"
        time = 0
        self.executing_time = 0
        while True:
            for i in self.gen.process_list:
                if i.arrive_t == time:
                    self.worklist.append(i)
            if self.executing_time == 0 and len(self.worklist) != 0:
                self.executing_time = self.worklist[0].exec_t
            time += 1
            if len(self.worklist) != 0:
                self.worklist[0].exec_t -= 1
                if self.worklist[0].exec_t == 0:
                    self.worklist[0].exec_t = self.executing_time
                    self.executing_time = 0
                    self.worklist[0].end_t = time
                    self.calculated_processes.append(self.worklist[0])
                    self.worklist.pop(0)
            if len(self.gen.process_list) == len(self.calculated_processes):
                self.gen.process_list = self.calculated_processes
                return time

    def sjf_simulation(self):
        if len(self.gen.process_list) == 0:
            return "Błąd!"
        time = 0
        self.executing_time = 0
        while True:
            for i in self.gen.process_list:
                if i.arrive_t == time:
                    self.worklist.append(i)
            if self.executing_time == 0 and len(self.worklist) != 0:
                self.executing_time = self.worklist[0].exec_t
            time += 1
            if len(self.worklist) != 0:
                self.worklist[0].exec_t -= 1
                if self.worklist[0].exec_t == 0:
                    self.worklist[0].exec_t = self.executing_time
                    self.executing_time = 0
                    self.worklist[0].end_t = time
                    self.calculated_processes.append(self.worklist[0])
                    self.worklist.pop(0)
                else:
                    for i in range(len(self.worklist)):
                        if i == 0 or i-1 == 0:
                            continue
                        if self.worklist[i].exec_t < self.worklist[i-1].exec_t:
                            self.worklist[i], self.worklist[i-1] = self.worklist[i-1], self.worklist[i]
            if len(self.gen.process_list) == len(self.calculated_processes):
                self.gen.process_list = self.calculated_processes
                return time

    def calculate_average_time(self):
        if len(self.gen.process_list) == 0:
            return "Błąd!"
        for i in range(len(self.calculated_processes)):
            if i == 0:
                self.waiting_times.append(0)
                continue
            self.waiting_times.append(abs(self.calculated_processes[i-1].end_t - self.calculated_processes[i].arrive_t))
        return sum(self.waiting_times) / len(self.calculated_processes)

    def calculate_standard_deviation(self):
        if len(self.waiting_times) == 0:
            return "Błąd!"
        return round(statistics.stdev(self.waiting_times), 2)
