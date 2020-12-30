import DataGenerator


x = DataGenerator.Generator(11)
x.generate_processes()
x.save_all()
x.load_all()
