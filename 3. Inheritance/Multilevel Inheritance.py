'''
Multilevel Inheritance allows us to create a hierarchical structure where a child class
can inherit from a parent class, which itself can inherit from another parent class.
The child class will then inherit attributes and methods from the parent classes.
Useful for building on top of various existing classes.

GameCharacter
    |
  Warrior
    |
  Knight
'''

class GameCharacter:
    def __init__(self, weapon = None):
        self.health = 100
        self.weapon = weapon
    
    def attack(self):
        print("attacked with a punch")

    def recover(self):
        print("recovered 10 HP")
        self.health = max(100, self.health + 10)

class Warrior(GameCharacter):
    def __init__(self):
        super().__init__("sword")
        self.raging = False

    def attack(self):
        print("slashed with a sword")
        if self.raging:
            print("slashed with a sword again")  
    
    def rage(self):
        print("increased attack power with rage")
        self.raging = True

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.weapon2 = "sword"
    
    def attack(self):
        print("double slashed with two swords")
        if self.raging:
            print("double slashed with two swords again")

# warrior = Warrior()
# print(warrior.weapon)
# warrior.rage()
# warrior.attack()

knight = Knight()
print(knight.weapon, knight.weapon2)
knight.rage()
knight.attack()
knight.recover()
