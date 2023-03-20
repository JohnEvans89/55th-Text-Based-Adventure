from Character.Character import *
from methods import *


class Player(Character):
    def __init__(self, name, hp, defense, attack, weapon, armor):
        Character.__init__(self, name, hp, defense, attack)
        self.maxHp = hp
        self.weapon = weapon
        self.armor = armor

inventory = {"ring": 0}


# def add_item(item, count):
#     inventory.update({item: count})
# def update_item(item, count):
#     inventory[item] += count


def add_item(item, count):
    if item in inventory.keys():
        inventory[item] += count
    else:
        inventory.update({item: count})


weapons = ["Rusted Sword", "Long Sword"]
weapon_damage = {"Rusted Sword": 10, "Long Sword": 10}

armors = ["Leather Tunic"]
armor_protection = {"Leather Tunic": 1}

play = Player("Test", 10, 0, 10, weapons[0], armors[0])


def player_status():
    clear()
    print("CHARACTER INFO")
    print_separator(20)
    print('{} [HP: {}/{}] [Weapon: {}] [Armor: {}]'.format(play.name, play.hp, play.maxHp, play.weapon, play.armor))
    print_separator(20)
    # print("")

def pick_name():
    name_question=input("What is your name?\n")
    name_choice=input("Is "+name_question+" your name?\n")
    if name_choice.upper()=="Y":
        play.name=name_question
    else:
        pick_name()

# pick_name()