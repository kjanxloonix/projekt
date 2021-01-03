import Generator
import TextMenu

menu = TextMenu.Menu()
generator = Generator.Generator()
generator.load_reference_list()
generator.show_reference_list()

menu.display()
menu.select()
menu.generatorclass_submenu()
