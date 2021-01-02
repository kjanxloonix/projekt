class Menu:
    def __init__(self):
        self.choice = 0
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
                print('\n+' + '-' * 13 + 'MENU' + '-' * 13 + '+')
            print('| ' + self.list[i] + ' |')
        else:
            print('+' + '-' * 30 + '+\n')

    def select(self):
        while True:
            try:
                self.choice = int(input("Wybierz >> "))
                if 0 < self.choice < 7:
                    return self.choice
                else:
                    print(" >Podaj poprawną liczbę.<")
                    continue
            except ValueError:
                print(" >Błędna wartość, podaj liczbę.<")

    def generatorclass_submenu(self):
        while True:
            self.choice = str(input("Czy chcesz edytować domyślne wartości generatora? [y/n] >> "))
            if self.choice == 'y' or self.choice == 'n':
                return self.choice
            else:
                print("Błąd. ", end='')
                continue

