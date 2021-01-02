import DataGenerator
import TextMenu
import Simulator

menu = TextMenu.Menu()
generator = DataGenerator.Generator()
simulator = Simulator.Simulator(generator)

# simulator.simulation()

while True:
    menu.display()
    select = menu.select()
    if select == 1:
        subselect = menu.generatorclass_submenu()
        if subselect == 'n':
            generator.generate_processes()
            generator.show_process_list()
        elif subselect == 'y':
            p, t1, t2 = menu.genetatorclass_submenu_handler()
            generator.generate_processes(p, t1, t2)
            generator.show_process_list()
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
