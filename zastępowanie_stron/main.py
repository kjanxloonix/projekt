import Generator
import TextMenu
import Simulator

menu = TextMenu.Menu()
generator = Generator.Generator()

def initiate_generator():
    subselect_g = menu.generatorclass_submenu()
    if subselect_g == 'y':
        size, begin, end = menu.generatorclass_submenu_handler()
        generator.generate_reference_list(size, begin, end)
    elif subselect_g == 'n':
        generator.generate_reference_list()

def generate_simulation():
    simulation = None
    subselect_s = menu.simulatorclass_submenu()
    if subselect_s == 'y':
        frames = menu.simulatorclass_submenu_handler()
        simulation = Simulator.Simulator(generator.reference_list, frames)
    elif subselect_s == 'n':
        simulation = Simulator.Simulator(generator.reference_list)
    return simulation


while True:
    menu.display()
    select = menu.select()
    if select == 1:
        initiate_generator()
    elif select == 2:
        generator.load_reference_list()
    elif select == 3:
        generator.save_reference_list()
    elif select == 4:
        simulator = generate_simulation()
        sim_time, times_swapped, times_omitted, counters = simulator.fifo_simulation()
        menu.simulatorclass_info_string(sim_time, times_swapped, times_omitted, counters)
    elif select == 5:
        simulator = generate_simulation()
        sim_time, times_swapped, times_omitted, counters = simulator.lru_simulation()
        menu.simulatorclass_info_string(sim_time, times_swapped, times_omitted, counters)
    elif select == 6:
        generator.show_reference_list()
    elif select == 7:
        print(" >Koniec działania programu.<")
        break
