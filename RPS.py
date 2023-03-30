import random
# RPS game for the ATC "enemy"
scissors_ascii = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.'''

paper_ascii = '''
    _______
   /      /,
  /      //
 /______//
(______(/'''

rock_ascii = '''
 _____
| | | |/\\
|_|_|_|\ \\
|        /
\_______/'''

def RPS_battle(comp,user):
  print(comp,"\n\t~~\n\tVS\n\t~~\n", user)


mylist = [rock_ascii,paper_ascii,scissors_ascii]

# comp_choice=random.choice(mylist)
# print(comp_choice)
# if comp_choice==rock_ascii:
#   print("Rock")
# elif comp_choice==paper_ascii:
#   print("Paper")
# elif comp_choice==scissors_ascii:
#   print("Scissors")
RPS_battle(rock_ascii,paper_ascii)