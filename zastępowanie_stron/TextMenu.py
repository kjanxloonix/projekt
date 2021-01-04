class Menu:
    def __init__(self):
        self.choice = 0
        self.options = []
        self.options.append("[1] Generuj nową listę odwołań")
        self.options.append("[2] Wczytaj listę odwołań     ")
        self.options.append("[3] Zapisz listę odwołań      ")
        self.options.append("[4] Symuluj algorytmem FIFO   ")
        self.options.append("[5] Symuluj algorytmem LRU    ")
        self.options.append("[6] Wyświetl listę odwołań    ")
        self.options.append("[7] Wyjdź z programu          ")
        self.infostrings_1 = []
        self.infostrings_1.append(" >Podaj poprawną wartość.<")
        self.infostrings_1.append(" >Błąd. Podaj liczbę.<")
        self.infostrings_1.append(" >Błędny zakres.<")
        self.infostrings_1.append("Czy chcesz edytować domyślne wartości generatora? [y/n] >> ")
        self.infostrings_1.append("Podaj rozmiar nowej listy. >> ")
        self.infostrings_1.append("Podaj początek zakresu dla generatora. >> ")
        self.infostrings_1.append("Podaj koniec zakresu dla generatora. >> ")
        self.infostrings_1.append("Czy chcesz edytować domyślną ilość ramek? [y/n] >> ")
        self.infostrings_1.append("Podaj ilość ramek dla symulatora. >> ")
        self.infostrings_2 = []
        self.infostrings_2.append("Czas trwania symulacji:")
        self.infostrings_2.append("\nLiczba podmian stron:")
        self.infostrings_2.append("\nIle razy odwołanie w ramce:")
        self.infostrings_2.append("\nLiczniki operacji na ramkach:")

    def display(self):
        for i in range(len(self.options)):
            if i == 0:
                print('\n+' + '-' * 14 + "MENU" + '-' * 14 + '+')
            print('| ' + self.options[i] + ' |')
        else:
            print('+' + '-' * 32 + '+\n')

    def select(self):
        while True:
            try:
                self.choice = int(input("Wybierz >> "))
                if 0 < self.choice < 8:
                    return self.choice
                else:
                    print(self.infostrings_1[0])
                    continue
            except ValueError:
                print(self.infostrings_1[1])

    def generatorclass_submenu(self):
        while True:
            self.choice = str(input(self.infostrings_1[3]))
            if self.choice == 'y' or self.choice == 'n':
                return self.choice
            else:
                print("Błąd. ", end='')
                continue

    def generatorclass_submenu_handler(self):
        while True:
            try:
                size = int(input(self.infostrings_1[4]))
                if size > 1:
                    break
                else:
                    print(self.infostrings_1[2])
            except ValueError:
                print(self.infostrings_1[1])

        while True:
            try:
                begin = int(input(self.infostrings_1[5]))
                if begin < 0:
                    print(self.infostrings_1[2])
                else:
                    break
            except ValueError:
                print(self.infostrings_1[1])

        while True:
            try:
                end = int(input(self.infostrings_1[6]))
                if begin >= end:
                    print(self.infostrings_1[2])
                else:
                    break
            except ValueError:
                print(self.infostrings_1[1])

        return size, begin, end

    def simulatorclass_submenu(self):
        while True:
            self.choice = str(input(self.infostrings_1[7]))
            if self.choice == 'y' or self.choice == 'n':
                return self.choice
            else:
                print("Błąd. ", end='')
                continue

    def simulatorclass_submenu_handler(self):
        while True:
            try:
                self.choice = int(input(self.infostrings_1[8]))
                if self.choice < 3:
                    print(self.infostrings_1[2])
                else:
                    break
            except ValueError:
                print(self.infostrings_1[1])
        return self.choice

    def simulatorclass_info_string(self, t1, t2, t3, c):
        print("{0}{1}{2}{3}{4}{5}{6}{7}".format(self.infostrings_2[0], str(t1), self.infostrings_2[1], str(t2),
                                                self.infostrings_2[2], str(t3), self.infostrings_2[3], str(c)))
