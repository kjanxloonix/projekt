import Generator
import TextMenu
import Simulator

menu = TextMenu.Menu()
generator = Generator.Generator()
simulator = None

while True:
    menu.display()
    select = menu.select()
    if select == 1:
        subselect_g = menu.generatorclass_submenu()
        if subselect_g == 'y':
            size, begin, end = menu.generatorclass_submenu_handler()
            generator.generate_reference_list(size, begin, end)
        elif subselect_g == 'n':
            generator.generate_reference_list()
    elif select == 2:
        generator.load_reference_list()
    elif select == 3:
        generator.save_reference_list()
    elif select == 4:
        # TODO funkcja oddzielna 1
        subselect_s = menu.simulatorclass_submenu()
        if subselect_s == 'y':
            frames = menu.simulatorclass_submenu_handler()
            simulator = Simulator.Simulator(generator.reference_list, frames)
        elif subselect_s == 'n':
            simulator = Simulator.Simulator(generator.reference_list)
        sim_time, times_swapped, times_omitted, counters = simulator.fifo_simulation()
        print("\nCzas trwania symulacji:", sim_time, "\nLiczba podmian stron:", times_swapped,
              "\nIle razy odwołanie w ramce:", times_omitted, "\nLiczniki operacji na ramkach:", counters)
    elif select == 5:
        # TODO funkcja oddzielna 2
        subselect_s = menu.simulatorclass_submenu()
        if subselect_s == 'y':
            frames = menu.simulatorclass_submenu_handler()
            simulator = Simulator.Simulator(generator.reference_list, frames)
        elif subselect_s == 'n':
            simulator = Simulator.Simulator(generator.reference_list)
        sim_time, times_swapped, times_omitted, counters = simulator.lru_simulation()
        print("\nCzas trwania symulacji:", sim_time, "\nLiczba podmian stron:", times_swapped,
              "\nIle razy odwołanie w ramce:", times_omitted, "\nLiczniki operacji na ramkach:", counters)
    elif select == 6:
        generator.show_reference_list()
    elif select == 7:
        print(" >Koniec działania programu.<")
        break
