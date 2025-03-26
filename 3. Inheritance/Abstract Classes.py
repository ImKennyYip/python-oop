'''
Inheritance - class hierarchy (ranking)

Parent (Base, Super) Class
Child (Derived, Sub/Supra) Class

Inheritance allows us to create (child) classes that are built upon existing (parent) classes.
However, sometimes we don't want to create instances of a parent class.
In that case, we can create an abstract base class with at least one abstract method.
Abstract base classes cannot be instantiated, and abstract methods must be overridden.
''' 
from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self):
        self.health = 100
        self.weapon = None

    @abstractmethod
    def attack(self):
        print("attacked with a punch")

    def recover(self):
        print("recovered 10 HP")
        self.health = max(100, self.health + 10)

class Warrior(GameCharacter):
    def attack(self):
        # super().attack()
        # GameCharacter.attack(self)
        print("slashed with a sword")

class Mage(GameCharacter): #Magician
    def attack(self):
        print("used a fire spell")

class Archer(GameCharacter):
    def attack(self):
        print("shot an arrow")

warrior = Warrior()
mage = Mage()
archer = Archer()
team = [warrior, mage, archer]

for member in team:
    member.attack()
    # member.recover()

# player = GameCharacter()
# player.attack()