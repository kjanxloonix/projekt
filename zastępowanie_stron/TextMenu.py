class Menu:
    def __init__(self):
        self.choice = 0
        self.list = []
        self.list.append("[1] Generuj nową listę odwołań")
        self.list.append("[2] Wczytaj listę odwołań     ")
        self.list.append("[3] Zapisz listę odwołań      ")
        self.list.append("[4] Symuluj algorytmem FIFO   ")
        self.list.append("[5] Symuluj algorytmem LRU    ")
        self.list.append("[6] Wyświetl listę odwołań    ")
        self.list.append("[7] Wyjdź z programu          ")
        self.strings = []
        self.strings.append(" >Podaj poprawną wartość.<")
        self.strings.append(" >Błąd. Podaj liczbę.<")
        self.strings.append(" >Błędny zakres.<")
        self.strings.append("Czy chcesz edytować domyślne wartości generatora? [y/n] >> ")
        self.strings.append("Podaj rozmiar nowej listy. >> ")
        self.strings.append("Podaj początek zakresu dla generatora. >> ")
        self.strings.append("Podaj koniec zakresu dla generatora. >> ")

    def display(self):
        for i in range(len(self.list)):
            if i == 0:
                print('\n+' + '-' * 14 + "MENU" + '-' * 14 + '+')
            print('| ' + self.list[i] + ' |')
        else:
            print('+' + '-' * 32 + '+\n')

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

    def generatorclass_submenu_handler(self):
        while True:
            try:
                size = int(input(self.strings[4]))
                if size > 1:
                    break
                else:
                    print(self.strings[2])
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
                else:
                    break
            except ValueError:
                print(self.strings[1])

        return size, begin, end



