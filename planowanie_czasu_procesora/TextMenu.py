class Menu:
    def __init__(self):
        self.list = []
        self.list.append("[1] Generuj listę procesów  ")
        self.list.append("[2] Załaduj listę procesów  ")
        self.list.append("[3] Zapisz listę procesów   ")
        self.list.append("[4] Symuluj algorytmem FCFS ")
        self.list.append("[5] Symuluj algorytmem SJF  ")
        self.list.append("[6] Wyjdź z programu        ")

    def display(self):
        for i in range(len(self.list)):
            if i == 0:
                print('+' + '-' * 13 + 'MENU' + '-' * 13 + '+')
            print('| ' + self.list[i] + ' |')
        else:
            print('+' + '-' * 30 + '+')

    def select(self):
        pass
