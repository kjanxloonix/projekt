import DataGenerator
import TextMenu


# x.generate_processes()
# x.save_all()
# x.load_all()
# x.show_process_list()

menu = TextMenu.Menu()
generator = DataGenerator.Generator()

while True:
    menu.display()
    select = menu.select()
    if select == 1:
        generator.generate_processes()
    elif select == 2:
        generator.load_all()
    elif select == 3:
        generator.save_all()
    elif select == 4:
        # TODO symulacja FCFS
        print('FCFS')
    elif select == 5:
        # TODO symulacja SJF
        print('SJF')
    elif select == 6:
        print(" >Koniec działania programu.<")
        break