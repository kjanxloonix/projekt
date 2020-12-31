import ProcessClass
import pickle
import random


class Generator:
    def __init__(self, number_of_processes=10):
        self.number = number_of_processes
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

    def generate_processes(self):
        print(" >Generuje nową listę procesów...<")
        for i in range(self.number):
            t1 = random.randrange(1, 10)
            t2 = random.randrange(1, 10)
            if i == 0:
                t1 = 0
            self.process_list.append(ProcessClass.Process(t1, t2))

    def show_process_list(self):
        index = 1
        for i in self.process_list:
            print("Process " + str(index) + ":", i.arrive_t, i.exec_t, i.end_t)
            index += 1
