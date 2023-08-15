class Bird:
    def __init__ (self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        return "Chirp"

class Duck(Bird):
    def sound(self):
        return "quack quack"

class Turkey(Bird):
    def sound(self):
        return "gobble, gobble"

duck = Duck("Mallard", "Duck")
turkey = Turkey("Christmas", "Turkey")

print(f"{duck.name} {duck.species} says: {duck.sound()}")
print(f"{turkey.name} {turkey.species}) says: {turkey.sound()}")
