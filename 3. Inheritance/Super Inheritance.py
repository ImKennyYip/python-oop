'''
Inheritance - class hierarchy

Parent (Base, Super) Class
Child (Derived, Sub/Supra) Class

super() allows a class to access a parent class method
parent = super class
super() returns a proxy instance of a parent class
'''

#parent class
class GameCharacter:
    def __init__(self, weapon=None):
        self.health = 100
        self.weapon = weapon

    def attack(self):
        print("attacked with a punch")

#child classes
class Warrior(GameCharacter):
    def __init__(self):
        # super().__init__()
        # self.weapon = "sword"
        # super().__init__() #overwrites weapon to None
        super().__init__("sword")

    def attack(self):
        if (self.weapon is None):
            #print("attacked with a punch")
            super().attack()
        else:
            print("slashed with a sword")
    
class Mage(GameCharacter): #Magician
    def __init__(self):
        super().__init__("staff")

    def attack(self):
        if (self.weapon is None):
            super().attack()
        else:
            print("used a fire spell")
        
class Archer(GameCharacter):
    def __init__(self):
        super().__init__("bow")

    def attack(self):
        if (self.weapon is None):
            super().attack()
        else:
            print("shot an arrow")

warrior = Warrior()
mage = Mage()
archer = Archer()
team = [warrior, mage, archer]

for member in team:
    print(member.health, member.weapon)
    member.attack()








''' 
class Warrior:
    def __init__(self):
        self.health = 100
        self.weapon = "sword"
    
    def attack(self):
        print("warrior slashed with sword")

class Mage: #Magician
    def __init__(self):
        self.health = 100
        self.weapon = "staff"
    
    def attack(self):
        print("mage used a fire spell")

class Archer:
    def __init__(self):
        self.health = 100
        self.weapon = "bow"

    def attack(self):
        self.shoot()

warrior = Warrior()
mage = Mage()
archer = Archer()

team = [warrior, mage, archer]

for member in team:
    member.attack()

'''
