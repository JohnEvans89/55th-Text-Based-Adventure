class Character(object):

  def __init__(self, name, hp, defense, attack):
    self.name = name
    self.hp = hp
    self.defense = defense
    self.attack = attack

  # def attack(self, other):
  #     pass

  def update(self):
    if self.hp < 0:
      self.dead = True
      self.hp = 0
