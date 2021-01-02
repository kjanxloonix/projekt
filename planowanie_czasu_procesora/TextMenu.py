class Menu:
    def __init__(self):
        self.choice = 0
        self.list = []
        self.list.append("[1] Generuj listę procesów  ")
        self.list.append("[2] Załaduj listę procesów  ")
        self.list.append("[3] Zapisz listę procesów   ")
        self.list.append("[4] Symuluj algorytmem FCFS ")
        self.list.append("[5] Symuluj algorytmem SJF  ")
        self.list.append("[6] Wyświetl listę procesów ")
        self.list.append("[7] Wyjdź z programu        ")
        self.strings = []
        self.strings.append(" >Podaj poprawną liczbę.<")
        self.strings.append(" >Błędna wartość, podaj liczbę.<")
        self.strings.append(" >Błędny zakres.<")
        self.strings.append("Czy chcesz edytować domyślne wartości generatora? [y/n] >> ")
        self.strings.append("Ile procesów chcesz wygenerować? >> ")
        self.strings.append("Podaj początek zakresu dla czasów nadejścia. >> ")
        self.strings.append("Podaj koniec zakresu dla czasów nadejścia. >> ")

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
                if 0 < self.choice < 8:
                    return self.choice
                else:
                    print(self.strings[0])
                    continue
            except ValueError:
                print(self.strings[1])

    def generatorclass_submenu(self):
        while True:
            self.choice = str(input(self.strings[3]))
            if self.choice == 'y' or self.choice == 'n':
                return self.choice
            else:
                print("Błąd. ", end='')
                continue

    def genetatorclass_submenu_handler(self):
        while True:
            try:
                processes = int(input(self.strings[4]))
                if processes < 3:
                    print(self.strings[2])
                    continue
                else:
                    break
            except ValueError:
                print(self.strings[1])

        while True:
            try:
                begin = int(input(self.strings[5]))
                if begin < 0:
                    print(self.strings[2])
                else:
                    break
            except ValueError:
                print(self.strings[1])

        while True:
            try:
                end = int(input(self.strings[6]))
                if begin >= end:
                    print(self.strings[2])
                    continue
                else:
                    break
            except ValueError:
                print(self.strings[1])

        return processes, begin, end