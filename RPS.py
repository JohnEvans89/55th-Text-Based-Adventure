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
print(rock_ascii, "\n\t~~\n\tVS\n\t~~\n", scissors_ascii)

import random

mylist = [rock_ascii,paper_ascii,scissors_ascii]

print(random.choice(mylist))
