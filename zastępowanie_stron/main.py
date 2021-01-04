import Generator
import TextMenu
import Simulator

menu = TextMenu.Menu()
generator = Generator.Generator()
generator.load_reference_list()
generator.show_reference_list()
simulator = Simulator.Simulator()
simulator.fifo_simulation()



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
#         # TODO FIFO SYMULACJA
#         print('FIFO')
#     elif select == 5:
#         # TODO LRU SYMULACJA
#         print('LRU')
#     elif select == 6:
#         generator.show_reference_list()
#     elif select == 7:
#         print(" >Koniec działania programu.<")
#         break
