from Character.Enemy import *

from Character.Player import *


# add random. figure out base stats + or - armor and weapon
def cross_road(n, e, s, w):
  while not is_valid:
    player_status()
    print(
      "You are at a crossroad.\n1: Go North\n2: Go East\n3: Go South\n4: Go West"
    )
    choice = prompt()
    if choice == '1':
      n()
    elif choice == '2':
      e()
    elif choice == '3':
      s()
    elif choice == '4':
      w()


def town_gate():
  player_status()
  print(
    "You are at the gate of the town.\nA guard is standing in front of you.\nWhat do you want to do?\n"
  )
  print("1: Talk to the guard\n2: Attack the guard\n3: Leave")
  choice = prompt()
  if choice == '1':
    player_status()
    if inventory['ring'] >= 1:
      print("You found a ring.\nCome on in")
      print("You won BITCH!!")
      quit()
    else:
      description_press_enter_method(
        "Guard: Hello there stranger. So your name is " + play.name + "?"
        "\nSorry but we cannot let a stranger enter our town."
        "\nA Goblin stole my wedding ring."
        "\nIf you get me it back, I will let you in.", town_gate)

  elif choice == '2':
    play.hp -= 1
    player_status()
    description_press_enter_method(
      "Guard: Hey don't be stupid.\nThe Guard hit you so hard you gave up.\n(You receive 1 damage)",
      town_gate)
  elif choice == '3':
    cross_road(river_side, long_sword, town_gate, goblin_fight)


def river_side():
  play.hp += 1
  player_status()
  # print("There is a river. You drink the water and rest at the riverside.\nYour HP is recovered +1\n")
  description_press_enter_method(
    "There is a river. You drink the water and rest at the riverside.\nYour HP is recovered +1\n",
    cross_road, river_side, long_sword, town_gate, goblin_fight)


def goblin_fight():
  player_status()
  print(
    "Goblin HP: {}\nYou come upon a Goblin.\nSomething shiny glitters on his finger"
    .format(goblin.hp))
  print("1: Fight\n2: Run")
  choice = prompt()
  if choice == '1':
    fight(goblin)
  else:
    cross_road(river_side, long_sword, town_gate, goblin_fight)


def long_sword():
  play.weapon = weapons[1]
  player_status()
  description_press_enter_method(
    "You walked into a forest and found a Long Sword!", cross_road, river_side,
    long_sword, town_gate, goblin_fight)


def fight(enemy):
  player_status()
  print("Goblin HP: {}".format(enemy.hp))
  print("1: Attack\n2: Run")
  choice = prompt()
  if choice == '1':
    attack(enemy)
  elif choice == '2':
    cross_road(river_side, long_sword, town_gate, goblin_fight)
  else:
    fight(enemy)


def attack(test):
  # if (myWeapon.equals("Rusted Sword")) {
  #     myAttack = attPow(0, 5);
  # if (myWeapon.equals("Long Sword")) {
  #     myAttack = attPow(5, 8);

  print("You attacked the {} and gave {} damage".format(
    test.name, weapon_damage[play.weapon]))
  test.hp -= weapon_damage[play.weapon]
  if test.hp < 1:
    win(test)

  if test.hp > 0:
    print("{} HP: {}".format(test.name, test.hp))
    mon_damage = test.attack - armor_protection[play.armor]
    play.hp -= mon_damage
    # monsterAttack = attPow(0, 4);
    description_press_enter("The {} attacks you. Your {} blocked {} points.\n"
                            "(You receive {} damage)".format(
                              test.name, play.armor,
                              armor_protection[play.armor], mon_damage))
    if play.hp < 1:
      print("You died")
      # dead()
    if play.hp > 0:
      fight(test)


def win(test):
  add_item(test.item, test.count)
  print(inventory['ring'])
  description_press_enter_method(
    "You killed the {}.\nYou obtained a silver ring!\n"
    "1: Go Back to Town".format(test.name, test.name), town_gate)


is_valid = False
# play = Player("Test", 10, 0, 10, weapon[0], armor[0])
# mon = Character("Goblin",15,0,5)
#

town_gate()
