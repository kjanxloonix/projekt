import DataGenerator
import TextMenu
import Simulator

menu = TextMenu.Menu()
generator = DataGenerator.Generator()

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
        simulator = Simulator.Simulator(generator)
        print("Czas wykonywania symulacji FCFS:", simulator.fcfs_simulation())
        print("Średni czas oczekiwania:", simulator.calculate_average_time())
        print("Odchylenie standardowe czasu oczekiwania:", simulator.calculate_standard_deviation())
    elif select == 5:
        simulator = Simulator.Simulator(generator)
        print("Czas wykonywania symulacji SJF:", simulator.sjf_simulation())
        print("Średni czas oczekiwania:", simulator.calculate_average_time())
        print("Odchylenie standardowe czasu oczekiwania:", simulator.calculate_standard_deviation())
    elif select == 6:
        generator.show_process_list()
    elif select == 7:
        print(" >Koniec działania programu.<")
        break
