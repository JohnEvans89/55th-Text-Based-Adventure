import random
import ascii as art



RPS_art = [art.rock_ascii, art.paper_ascii, art.scissors_ascii]

def RPS_player_choice():
  player_choice=input("Make Your Choice: \n\t1. Rock\n\t2. Paper\n\t3. Scissors\n--->")

# RPS game for the ATC "enemy"
def RPS_battle(comp, user):
  comp_choice = random.choice(RPS_art)
  print(comp, "\n\t~~\n\tVS\n\t~~\n", user)
  if comp=="Rock\n"+art.rock_ascii:
    print("works")

# This is probably not needed. The main functionalitty is just the random.choice
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

# RPS_battle(computer_player(),"computer_player()")
RPS_player_choice()
def ATC_53():
  print("*** insert ascii ***")
  print("")

print(art.ATC_ascii,art.paper_ascii_2)