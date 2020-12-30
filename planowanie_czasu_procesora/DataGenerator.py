import ProcessClass
import pickle


class Generator:
    def __init__(self, number=10):
        self.number_of_processes = number
        self.process_list = []

    def save_all(self):
        file = open('samples', 'wb')
        pickle.dump(self.process_list, file)
        file.close()
        print("Zapisano dane do pliku.")

    def load_all(self):
        file = open('samples', 'rb')
        self.process_list = pickle.load(file)
        print("Załadowano dane z pliku.")

    def generate_processes(self):
        self.process_list.append(ProcessClass.Process(1, 2, 3))
        self.process_list.append(ProcessClass.Process(4, 5, 6))
