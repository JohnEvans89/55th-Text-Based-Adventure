import random
import ascii as art

RPS_art = [art.rock_ascii, art.paper_ascii, art.scissors_ascii]


# RPS game for the ATC "enemy"
def RPS_battle(comp, user):
  print(comp, "\n\t~~\n\tVS\n\t~~\n", user)
  if comp=="Rock\n"+art.rock_ascii:
    print("works")


def computer_player():
  comp_choice = random.choice(RPS_art)
  # print(comp_choice)
  if comp_choice == art.rock_ascii:
    comp_choice="Rock\n"+comp_choice
  elif comp_choice == art.paper_ascii:
    comp_choice="Paper\n"+comp_choice
  elif comp_choice == art.scissors_ascii:
    comp_choice="Scissors\n"+comp_choice
  else:
    print("Something broke!!!")
  return comp_choice


# RPS_battle(art.rock_ascii,art.scissors_asci)

RPS_battle(computer_player(),"computer_player()")
