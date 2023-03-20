from Character.Character import *
from methods import *


class Enemy(Character):

  def __init__(self, name, hp, defense, attack, item, count):
    Character.__init__(self, name, hp, defense, attack)
    self.item = item
    self.count = count

  # def attack(self, other):
  #     pass


goblin = Enemy("Goblin", 15, 0, 5, "ring", 1)
