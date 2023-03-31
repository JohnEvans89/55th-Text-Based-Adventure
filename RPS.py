import random
import ascii as art
# RPS game for the ATC "enemy"
def RPS_battle(comp,user):
  print(comp,"\n\t~~\n\tVS\n\t~~\n", user)


mylist = [art.rock_ascii,art.paper_ascii,art.scissors_ascii]

def computer_player():
  comp_choice=random.choice(mylist)
  print(comp_choice)
  if comp_choice==art.rock_ascii:
    print("Rock")
  elif comp_choice==art.paper_ascii:
    print("Paper")
  elif comp_choice==art.scissors_ascii:
    print("Scissors")
  else:
    print("Something broke!!!")
# RPS_battle(art.rock_ascii,art.scissors_asci)
p=0
while p<5:
  computer_player()
  p+=1
  