import Generator
import TextMenu
import Simulator

menu = TextMenu.Menu()
generator = Generator.Generator()
generator.load_reference_list()
generator.generate_reference_list()
generator.show_reference_list()
simulator = Simulator.Simulator(generator.reference_list)
simulator.lru_simulation()


# while True:
#     menu.display()
#     select = menu.select()
#     if select == 1:
#         subselect = menu.generatorclass_submenu()
#         if subselect == 'y':
#             size, begin, end = menu.generatorclass_submenu_handler()
#             generator.generate_reference_list(size, begin, end)
#         elif subselect == 'n':
#             generator.generate_reference_list()
#     elif select == 2:
#         generator.load_reference_list()
#     elif select == 3:
#         generator.save_reference_list()
#     elif select == 4:
#         simulator = Simulator.Simulator(generator.reference_list)
#         sim_time, times_swapped, times_omitted = simulator.fifo_simulation()
#         print("\nCzas trwania symulacji:", sim_time, "\nLiczba podmian stron:", times_swapped,
#               "\nIle razy odwołanie w ramce:", times_omitted)
#     elif select == 5:
#         # TODO LRU SYMULACJA
#         print('LRU')
#     elif select == 6:
#         generator.show_reference_list()
#     elif select == 7:
#         print(" >Koniec działania programu.<")
#         break
