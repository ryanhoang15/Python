class Mammal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("I am a {}".format(self.species))


class Dog(Mammal):
    def makesounds(self):
        print("Woof! Woof!")


class Cat(Mammal):
    def makesounds(self):
        print("Meow")


x = Dog("Dog")
y = Cat("Cat")
poly = [x, y]
for obj in poly:
    obj.show_species()
    obj.makesounds()