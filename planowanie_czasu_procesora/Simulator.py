import DataGenerator

class Simulator:
    def __init__(self, generator, algorithm=''):
        self.gen = generator
        self.alg = algorithm
    def simulation(self):
        for i in range(10):
            print(',')