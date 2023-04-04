import random
import ascii as art
import os
RPS_art = [art.rock_ascii_2]


def RPS_player_choice():
  player_choice = input(
    "Make Your Choice: \n\t1. Rock\n\t2. Paper\n\t3. Scissors\n--->")
  if player_choice == '1': return art.rock_ascii_2
  elif player_choice == '2': return art.paper_ascii_2
  else: return art.scissors_ascii_2


# RPS game for the ATC "enemy"
def RPS_battle():
  win=0
  lose=0
  while True:
    print(f"Wins: {win} Loses: {lose}")
    user = RPS_player_choice()
    comp_choice = random.choice(RPS_art)
    print(user, "\n\t~~\n\tVS\n\t~~\n", comp_choice)
    if user == comp_choice:
      print("Draw")
    elif (user==art.rock_ascii_2 and comp_choice==art.scissors_ascii_2) or (user==art.scissors_ascii_2 and comp_choice==art.paper_ascii_2) or (user==art.paper_ascii_2 and comp_choice==art.rock_ascii_2):
      print("you win")
      win +=1
      if win>=3:
        # break
        return "w"
    else:
      print("lose")
      lose +=1
      if lose>=3:
        # break
        return "l"




def ATC_53():
  print(art.ATC_ascii)
  print(
    'Looking for an entrance to the building...\nAn ATC Airman appears\n\t"To get to the unit, you\'ll have to beat me...at Rock Paper Scissors!"'
  )


# print(art.ATC_ascii,art.paper_ascii_2)
# ATC_53()
# print(random.choice(RPS_art))


RPS_battle()
