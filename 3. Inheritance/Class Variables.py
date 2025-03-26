'''
Class Variables are single values shared by all instances of a class
Instance Variables (data members, fields, attributes) are unique to the instance of a class

'''

class Warrior:
    money = 0

    def __init__(self):
        self.health = 100  #instance variables
        self.weapon = None
        Warrior.money += 500

warrior1 = Warrior()
warrior2 = Warrior()
warrior3 = Warrior()

team = [warrior1, warrior2, warrior3]
warrior1.health -= 50
sword_price = 300

for member in team:
    if (Warrior.money >= sword_price):
        Warrior.money -= sword_price
        member.weapon = "sword"
    print(member.health, member.weapon, Warrior.money)
