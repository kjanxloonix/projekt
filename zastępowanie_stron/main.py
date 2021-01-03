import Generator
import TextMenu

menu = TextMenu.Menu()
generator = Generator.Generator()
# generator.load_reference_list()
# generator.show_reference_list()
#
# menu.display()
# select = menu.select()
# subselect = menu.generatorclass_submenu()

while True:
    menu.display()
    select = menu.select()
    if select == 1:
        generator.generate_reference_list()
    elif select == 2:
        generator.load_reference_list()
    elif select == 3:
        generator.save_reference_list()
    elif select == 4:
        # TODO FIFO SYMULACJA
        print('FIFO')
    elif select == 5:
        # TODO LRU SYMULACJA
        print('LRU')
    elif select == 6:
        generator.show_reference_list()
    elif select == 7:
        print(" >Koniec działania programu.<")
        break
