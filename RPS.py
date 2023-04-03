import random
import ascii as art

RPS_art = [art.rock_ascii_2, art.paper_ascii_2, art.scissors_ascii_2]


def RPS_player_choice():
  player_choice = input(
    "Make Your Choice: \n\t1. Rock\n\t2. Paper\n\t3. Scissors\n--->")
  if player_choice == '1': return art.rock_ascii_2
  elif player_choice == '2': return art.paper_ascii_2
  else: return art.scissors_ascii_2


# RPS game for the ATC "enemy"
def RPS_battle():
  user=RPS_player_choice()
  win_lose=user
  user_choice = ''
  comp_choice = random.choice(RPS_art)
  if user == 'r': user_choice = art.rock_ascii_2
  elif user == 'p': user_choice = art.paper_ascii_2
  else: user_choice = art.scissors_ascii_2
  print(comp_choice, "\n\t~~\n\tVS\n\t~~\n", user_choice)
  # if win_lose=='r' and 
def ATC_53():
  print(art.ATC_ascii)
  print(
    'Looking for an entrance to the building...\nAn ATC Airman appears\n\t"To get to the unit, you\'ll have to beat me...at Rock Paper Scissors!"'
  )


# print(art.ATC_ascii,art.paper_ascii_2)
# ATC_53()
# print(random.choice(RPS_art))
n = 5
while n > 0:
  print(n)
  print(RPS_player_choice())
  n -= 1
