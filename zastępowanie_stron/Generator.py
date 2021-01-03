import pickle
import random

class Generator:
    def __init__(self):
        self.reference_list = []

    def save_reference_list(self):
        file = open('samples2', 'wb')
        pickle.dump(self.reference_list, file)
        file.close()
        print(" >Zapisano listę odwołań do pliku.<")

    def load_reference_list(self):
        file = open('samples2', 'rb')
        self.reference_list = pickle.load(file)
        print(" >Załadowano listę odwołań z pliku.<")

    def show_reference_list(self):
        print("Długość listy odwołań:", len(self.reference_list))
        for i in self.reference_list:
            print(i, end=' ')
        else:
            print()

    def generate_reference_list(self, size=10, begin=0, end=10):
        print(" >Generuję nową listę odwołań...<")
        self.reference_list.clear()
        for i in range(size):
            value = random.randrange(begin, end)
            self.reference_list.append(value)
