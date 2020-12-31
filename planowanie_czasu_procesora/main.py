import DataGenerator
import TextMenu
import Simulator

menu = TextMenu.Menu()
generator = DataGenerator.Generator()
simulator = Simulator.Simulator(generator)

simulator.simulation()

# while True:
#     menu.display()
#     select = menu.select()
#     if select == 1:
#         generator.generate_processes()
#     elif select == 2:
#         generator.load_all()
#     elif select == 3:
#         generator.save_all()
#     elif select == 4:
#         # TODO symulacja FCFS
#         print('FCFS')
#     elif select == 5:
#         # TODO symulacja SJF
#         print('SJF')
#     elif select == 6:
#         print(" >Koniec działania programu.<")
#         break
