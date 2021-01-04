class Menu:
    def __init__(self):
        self.choice = 0
        self.options = []
        self.options.append("[1] Generuj listę procesów  ")
        self.options.append("[2] Załaduj listę procesów  ")
        self.options.append("[3] Zapisz listę procesów   ")
        self.options.append("[4] Symuluj algorytmem FCFS ")
        self.options.append("[5] Symuluj algorytmem SJF  ")
        self.options.append("[6] Wyświetl listę procesów ")
        self.options.append("[7] Wyjdź z programu        ")
        self.infostrings = []
        self.infostrings.append(" >Podaj poprawną liczbę.<")
        self.infostrings.append(" >Błędna wartość, podaj liczbę.<")
        self.infostrings.append(" >Błędny zakres.<")
        self.infostrings.append("Czy chcesz edytować domyślne wartości generatora? [y/n] >> ")
        self.infostrings.append("Ile procesów chcesz wygenerować? >> ")
        self.infostrings.append("Podaj początek zakresu dla czasów nadejścia. >> ")
        self.infostrings.append("Podaj koniec zakresu dla czasów nadejścia. >> ")

    def display(self):
        for i in range(len(self.options)):
            if i == 0:
                print('\n+' + '-' * 13 + 'MENU' + '-' * 13 + '+')
            print('| ' + self.options[i] + ' |')
        else:
            print('+' + '-' * 30 + '+\n')

    def select(self):
        while True:
            try:
                self.choice = int(input("Wybierz >> "))
                if 0 < self.choice < 8:
                    return self.choice
                else:
                    print(self.infostrings[0])
                    continue
            except ValueError:
                print(self.infostrings[1])

    def generatorclass_submenu(self):
        while True:
            self.choice = str(input(self.infostrings[3]))
            if self.choice == 'y' or self.choice == 'n':
                return self.choice
            else:
                print("Błąd. ", end='')
                continue

    def genetatorclass_submenu_handler(self):
        while True:
            try:
                processes = int(input(self.infostrings[4]))
                if processes < 3:
                    print(self.infostrings[2])
                    continue
                else:
                    break
            except ValueError:
                print(self.infostrings[1])

        while True:
            try:
                begin = int(input(self.infostrings[5]))
                if begin < 0:
                    print(self.infostrings[2])
                else:
                    break
            except ValueError:
                print(self.infostrings[1])

        while True:
            try:
                end = int(input(self.infostrings[6]))
                if begin >= end:
                    print(self.infostrings[2])
                    continue
                else:
                    break
            except ValueError:
                print(self.infostrings[1])

        return processes, begin, end
