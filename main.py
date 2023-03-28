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
    "This will be an adventure game. See if you can make it to \nthe bay in time for morning formation.\nBut don't run into the Commander or you will be ELS'd\n\n!!!ALSO WATCH OUT FOR SOLDIERS!!!"
  )
  prCyan("―" * 30)
  print(" * " * 10)
  prCyan("―" * 30)
  press_enter(["key"])


def pick_name():
  straight_line()
  test = input(
    "Sorry, our paperwork is jacked up.\nWhat was your name again Airman?\n")
  check = input(test + " is that right? (Y or N)\n")
  if check.upper() == 'Y' or not check:
    return test.upper()
  else:
    pick_name()


def cross_roads(left, right, forward, back):
  straight_line()
  print(f"1.Left\n2.Right\n3.Forward\n4.Back")
  print("1.Left", left, '\n2.Right', str(right), '\n3.Forward', forward,
        '\n4.Back', back)

  choice = input("Where do you want to go?\n")
  if choice == '2':
    right()
  else:
    print("didn't work" + choice)


def car_to_door():
  straight_line()
  if inventory["key"] == 0:
    print(
      'You walk from your car and notice\nthat the parking lot is already full.\nYou walk up to the doors of the building and try to open the door.\n\nOH NO!!!!!\nTHE DOOR IS LOCKED!!!!!\n\nYour phone rings, it\'s MSgt. Osbourne:\n\t"Airman',
      play.name,
      'where are you?"\n\t"Morning formation is about to occur. Get in here!"')
    # cross_roads()
  else:
    print("The key unlocked the door\nYou enter the building")
    press_enter()


# ------------------------------------------------------#
# ------------------------------------------------------#



def dumpster():
  # straight_line()
  if not inventory["key"] == 0:
    print("The soldier has left. Head towards the buiding")
    press_enter()
    car_to_door
  else:
    print('You go right, looking for a way into the building.\nAs you near the dumpsters...')
    print(soldier,'\nAN ANGRY SOLDIER JUMPS OUT OF THE DUMPSTER!!\n\t"Oh look, a lost Airman"\n\t"I stole the key to your precious unit."\n\t"Play me in hangman for the key or else!"\n\t"You have 5 guesses (HINT:Slogan)"')
    press_enter()
    hangman()
    
    
    
if __name__ == '__main__':
  # greeting()
  # play.name = pick_name()
  # car_to_door()
  dumpster()
  # db_ask_question("q1")
  # cross_roads("35ATC", dumpster, "5", "y")
