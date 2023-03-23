from methods import *

class Airman(object):
  def __init__(self, name):
    self.name=name


inventory = {"XCOMM Patch": 0, 'Squadron Patch':0,'key':0}


# def add_item(item, count):
#     inventory.update({item: count})
# def update_item(item, count):
#     inventory[item] += count



def add_item(item, count):
    if item in inventory.keys():
        inventory[item] += count
    else:
        inventory.update({item: count})
      
play = Airman("Test")



