from challenge import *

def greeting():
  prCyan("―" * 30)
  print(" * " * 10)
  prCyan("―" * 30)
  prRed('''
        WELCOME TO THE 
        55th COMBAT COMMUNICATION
        SQUADRON
        ''')
  prRed(
    "This will be an adventure game. See if you can make it to \nthe bay in time for morning formation.\nBut don't run into the Commander or you will be Discharged\n\n!!!ALSO WATCH OUT FOR SOLDIERS!!!"
  )
  prCyan("―" * 30)
  print(" * " * 10)
  prCyan("―" * 30)
  press_enter()


def pick_name():
  straight_line()
  test = input(
    "Sorry, our paperwork is jacked up.\nWhat was your name again Airman?\n")
  check = input(test + " is that right? (Y or N)\n")
  if check.upper() == 'Y' or not check:
    return test.upper()
  else:
    pick_name()


def cross_roads_4(left, right, forward, back):
  straight_line()
  print(f"1.Left\n2.Right\n3.Forward\n4.Back")


def cross_roads_2(one_direction,one_method, two_direction, two_method):
  straight_line()
  print(f"1. {one_direction} \n2. {two_direction}")
  choice = input("Where do you want to go?\n")
  if choice == '1':
    one_method()
  if choice == '2':
    two_method()
  else:
    print("didn't work" + choice)


def car_to_door():
  straight_line()
  print(basicbuilding_ascii)
  if inventory["key"] == 0:
    print(
      'You walk from your car and notice\nthat the parking lot is already full.\nYou walk up to the doors of the building and try to open the door.\n\nOH NO!!!!!\nTHE DOOR IS LOCKED!!!!!\n\nYour phone rings, it\'s MSgt. Osbourne:\n\t"Airman',
      play.name,
      'where are you?"\n\t"Morning formation is about to occur. Get in here!"')
    press_enter()
    # cross_roads()
  else:
    print("The key unlocked the door\nYou enter the building")
    press_enter()


# ------------------------------------------------------#
# ------------------------------------------------------#


def dumpster():
  straight_line()
  if not inventory["key"] == 0:
    print("The soldier has left. Head towards the buiding")
    press_enter()
    car_to_door
  else:
    print(
      'You go right, looking for a way into the building.\nAs you near the dumpsters...'
    )
    press_enter()
    print(
      soldier_ascii,
      '\nAN ANGRY SOLDIER JUMPS OUT OF THE DUMPSTER!!\n\t"Oh look, a lost Airman"\n\t"I stole the key to your precious unit."\n\t"Play me in hangman for the key or else!"\n\t"You have 5 guesses (HINT:Slogan)"'
    )
    press_enter()
    t = hangman()
    if t == True:
      add_item('key', 1)
      straight_line()
      
      print(soldier_lose,
        '\n\t"Ahhh. You guessed it."\n\t"HERE!!!"\nSoldier gave you the key\nHead back to building.'
      )
      press_enter()
      car_to_door()
    else:
      straight_line()
      print(
        '"\tHahaha You guessed wrong."\nThe soldier disappeared with the key.\nFind another way in.'
      )
      press_enter()
      # ATC()


if __name__ == '__main__':
  # greeting()
  # play.name = pick_name()
  car_to_door()
  # cross_roads_2("Left",pick_name, "Right",dumpster)
