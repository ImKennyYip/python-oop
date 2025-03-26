'''
Diamond Inheritance Problem occurs with Multiple Inheritance

    GameCharacter
        /   \
    Warrior Mage
        \   /           
    MagicWarrior

Occurs when there is a method conflict. 
which constructor to call? which method to call?
C++ -> can be resolved with virtual inheritance
Java -> no support for multiple inheritance; however problem can occur with multiple interfaces
Python -> resolved with method resolution order (MRO) - left to right from bottom to top
''' 

#parent class
class GameCharacter:
    def __init__(self, weapon=None):
        # print("GameCharacter __init__")
        self.health = 100
        self.weapon = weapon

    def attack(self):
        print("attacked with a punch")

class Warrior(GameCharacter):
    def __init__(self):
        # print("Warrior __init__")
        GameCharacter.__init__(self, "sword")

    def attack(self):
        print("Warrior attack")
        if (self.weapon is None):
            GameCharacter.attack(self)
        else:
            print("slashed with a sword")
    
class Mage(GameCharacter): #Magician
    def __init__(self):
        # print("Mage __init__")
        GameCharacter.__init__(self, "staff")

    def attack(self):
        print("Mage attack")
        if (self.weapon is None):
            GameCharacter.attack(self)
        else:
            print("used a fire spell")

class MagicWarrior(Warrior, Mage):
    pass

# print(MagicWarrior.mro())
magic_warrior = MagicWarrior()
magic_warrior.weapon = None
print(magic_warrior.weapon)
magic_warrior.attack()