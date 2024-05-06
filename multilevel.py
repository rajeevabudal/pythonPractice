class Animal:
    def __init__(self, species, name):
        self.species = species;
        self.name = name;

    def printName(self):
        print("Species = "+" " +self.species);
        print("Species = " + " " + self.name);


class Breed(Animal):
    def __init__(self, breed, name):
        Animal.__init__(self,species,name)
        self.breed = breed;

    def printName(self):
        Animal.printName(self)
        print("Species = " + " " + self.breed);

class type(Breed):
    def __init__(self, color):
        self.name = color;


    def printName(self):
        Breed.printName(self)
        print("Species = " + " " + self.color);


o = type("dog", "lavaode", "blak")
o.printName();