from methods import *

name = 'popo'


def greeting():
    prCyan("―" * 30)
    print(" * " * 10)
    prCyan("―" * 30)
    prRed(
        '''
        WELCOME TO THE 
        55th COMBAT COMMUNICATION
        SQUADRON
        ''')
    prRed(
        "This will be an adventure game. See if you can make it to \nthe bay in time for morning formation.\nBut don't run into the Commander or you will be ELS'd\n\n!!!ALSO WATCH OUT FOR SOLDIERS!!!")
    prCyan("―" * 30)
    print(" * " * 10)
    prCyan("―" * 30)
    press_enter()


def pick_name():
    straight_line()
    test = input("Sorry, our paperwork is jacked up.\nWhat was your name again Airman?\n")
    check = input(test + " is that right? (Y or N)\n")
    if check.upper() == 'Y' or check == '':
        return test.upper()
    else:
        pick_name()


def cross_roads(N, S, E, W):
    straight_line()
    choice = input("Where do you want to go?")
    print('1. Go Left\n2. Go Forward\n3. ')
    print(W)
    print(E)
    print(S)


def car_to_door():
    straight_line()
    print(
        'You walk from your car and notice\nthat the parking lot is already full.\nYou walk up to the doors of the building and try to open the door.\n\nOH NO!!!!!\nTHE DOOR IS LOCKED!!!!!\n\nYour phone rings, it\'s MSgt. Osbourne:\n\t"Airman',
        name,
        'where are you?"\n\t"Morning formation is about to occur. Get in here!"')


# ------------------------------------------------------#
# ------------------------------------------------------#


if __name__ == '__main__':
    greeting()
    name = pick_name()
    car_to_door()
