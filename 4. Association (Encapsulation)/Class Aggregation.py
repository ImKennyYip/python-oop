'''
Association describes relationships between classes:
Aggregation implies a relationship where a class can exist independently of another class
Composition implies a relationship where a class cannot exist independently of another class

Inheritance: Class A IS Class B, (A inherits B)
Association:
    Composition: Class A OWNS Class B
    Aggregation: Class A HAS Class B
'''
class Sword:
    def __init__(self):
        self.category = Warrior

class Bow:
    def __init__(self):
        self.category = Archer

class Archer:
    pass

class Warrior:
    def __init__(self):
        self.health = 100
        self.weapon = None #"sword"
    
    def attack(self):
        if isinstance(self.weapon, Sword):
            print("slashed with a sword")
        else:
            print("attacked with a punch")
    
    def equip(self, weapon):
        if isinstance(self, weapon.category):
            print("equipped weapon")
            self.weapon = weapon
        else:
            print("cannot equip this weapon")

sword = Sword()
bow = Bow()

warrior = sword.category()
warrior.attack()
warrior.equip(bow)
warrior.equip(sword)
warrior.attack()
