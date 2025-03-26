'''
Nested Classes allow one class to be defined inside another class.
This is useful if a specific class is ever only used by another class
and is not declared outside that class.
'''

class Dragon:
    def attack(self):
        print("used a dark fire breath attack")

class Mage: #Magician
    class Dragon:
        def attack(self):
            print("used a fire breath attack")

    def __init__(self):
        self.health = 100
        self.weapon = "staff"
        self.dragon = None
    
    def attack(self):
        print("used a fire spell")
        if (self.dragon is not None):
            self.dragon.attack()
    
    def summon_dragon(self):
        if (self.dragon is None):
            print("summoned dragon")
            self.dragon = Mage.Dragon()

mage = Mage()
mage.summon_dragon()
mage.attack()

enemy_dragon = Dragon()
enemy_dragon.attack()
