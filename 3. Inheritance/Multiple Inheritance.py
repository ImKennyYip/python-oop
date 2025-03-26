'''
Inheritance - class hierarchy (ranking)

Parent (Base, Super) Class
Child (Derived, Sub/Supra) Class

Multiple Inheritance allows a child class to inherit from multiple parents.
A child class can inherit from multiple parent classes, and their parents as well (multilevel).

Multilevel: A -> B -> C
Multiple: A, B -> C
''' 

#parent class
class GameCharacter:
    def __init__(self, weapon=None):
        self.health = 100
        self.weapon = weapon

    def attack(self):
        print("attacked with a punch")

class Warrior(GameCharacter):
    def __init__(self):
        # super().__init__("sword")
        super().__init__()
        self.weapon = "sword"

    def attack(self):
        if (self.weapon is None):
            super().attack()
        else:
            print("slashed with a sword")
    
class Mage(GameCharacter): #Magician
    def __init__(self):
        # super().__init__("staff")
        super().__init__()
        self.weapon = "staff"

    def attack(self):
        if (self.weapon is None):
            super().attack()
        else:
            print("used a fire spell")

class MagicWarrior(Warrior, Mage):
    def __init__(self):
        # super().__init__()
        Warrior.__init__(self)
        self.weapon2 = "staff"
    
    def attack(self):
        Warrior.attack(self)
        Mage.attack(self)

magic_warrior = MagicWarrior()
print(magic_warrior.weapon, magic_warrior.weapon2)
magic_warrior.attack()