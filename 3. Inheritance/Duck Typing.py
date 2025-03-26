'''
"If it walks like a duck and it quacks like a duck, then it must be a duck"
Don't care that an object is a duck, only care that it quacks.
Duck Typing is a form of polymorphism where different classes can share similar behaviors.
''' 

class Warrior:
    def __init__(self):
        self.health = 100
        self.weapon = "sword"
    
    # def slash(self):
    #     print("warrior slashed with sword")
    
    def attack(self):
        print("warrior slashed with sword")
    
class Mage: #Magician
    def __init__(self):
        self.health = 100
        self.weapon = "staff"
    
    # def spell(self):
    #     print("mage used a fire spell")
    
    def attack(self):
        print("mage used a fire spell")
        
class Archer:
    def __init__(self):
        self.health = 100
        self.weapon = "bow"
        
    # def shoot(self):
    #     print("archer shot an arrow")

    def attack(self):
        print("archer shot an arrow")

warrior = Warrior()
mage = Mage()
archer = Archer()

team = [warrior, mage, archer]

for member in team:
    # member.slash()
    member.attack()