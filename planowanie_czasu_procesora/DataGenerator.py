import ProcessClass
import pickle
import random

class Generator:
    def __init__(self):
        self.process_list = []

    def save_all(self):
        file = open('samples', 'wb')
        pickle.dump(self.process_list, file)
        file.close()
        print(" >Zapisano dane do pliku.<")

    def load_all(self):
        file = open('samples', 'rb')
        self.process_list = pickle.load(file)
        print(" >Załadowano dane z pliku.<")

    def generate_processes(self, processes_number=10, begin=0, end=10):
        print(" >Generuje nową listę procesów...<")
        self.process_list.clear()
        for i in range(processes_number):
            t_arr = random.randrange(begin, end)
            t_exec = random.randrange(1, 20)
            self.process_list.append(ProcessClass.Process(t_arr, t_exec))

    def show_process_list(self):
        print("Długość listy procesów:", len(self.process_list))
        index = 1
        for i in self.process_list:
            print("Proces " + str(index) + ":", i.arrive_t, i.exec_t, i.end_t)
            index += 1
