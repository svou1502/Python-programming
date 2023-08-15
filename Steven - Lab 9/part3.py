"""name and species are encapsulated in this class"""

from typing import Generic


class Bird:
    def __init__ (self, name, species):
        self.name = name
        self.species = species

    def sound(self): # This is abstract, really only used as an example, can't be recalled
        return "Chirp"

"""Using inheritance so the Owl and Dod class inherit
attributes from the parent Bird class"""

class Owl(Bird):
    def sound(self):
        return "Hoot Hoot"

"""Using polymorphism to overide the sound function 
from the parent class (Bird)"""

class Dodo(Bird):
    def sound(self):
        return "I am extinct, I make no sound"

class Generic_Bird(Bird):
    def sound(self):
        return "cheep cheep"

owl = Owl("Barn", "Owl")
dodo = Dodo("Extinct", "Dodo")
generic_bird = Generic_Bird("Every other", "Bird")

print(f"{owl.name} {owl.species} says: {owl.sound()}")
print(f"{dodo.name} {dodo.species} says: {dodo.sound()}")
print(f"Every other bird says: {generic_bird.sound()}")
