'''
Association describes relationships between classes:
Aggregation implies a relationship where a class can exist independently of another class
Composition implies a relationship where a class cannot exist independently of another class

Inheritance: Class A IS Class B, (A inherits B)
Association:
    Composition: Class A OWNS Class B
    Aggregation: Class A HAS Class B
'''
class Dragon:
    def attack(self):
        print("used a fire breath attack")

class Mage: #Magician
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
            self.dragon = Dragon()

mage = Mage()
mage.summon_dragon()
mage.attack()

mage = None