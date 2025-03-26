'''
Inheritance - class hierarchy (ranking)

Parent (Base, Super) Class
Child (Derived, Sub/Supra) Class

Inheritance allows us to create (child) classes that are built upon existing (parent) classes.
Inheritance promotes code reuse as child classes inherit all attributes and methods from parent classes
The parent class is usually used as an interface for various child classes
''' 

class GameCharacter:
    def __init__(self):
        self.health = 100
        self.weapon = None
        self.level = 1
        self.experience = -100
    
    def attack(self):
        print("attacked with a punch")
    
    def recover(self):
        print("recovered 10 HP")
        self.health = max(100, self.health + 10)


class Warrior(GameCharacter):
    def attack(self):
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
    print(member.health, member.weapon, member.level, member.experience)
    if member.health < 60:
        member.recover()
    else:
        member.attack()

