from replit import db

# ____
# DB
# ____
def load_db():
  db["q1"] = {
    "Question 1": "Who is the 55th CBCS Commander",
    '1': 'Col. Garrison',
    '2': 'Lt. Col. Williams',
    '3': 'Maj. Spikes',
    '4': 'Capt. Ifan',
    'Answer': '2'
  }
  
  db["q2"] = {
    'Question 2': 'What is our Group?',
    '1': '338th',
    '2': '336th',
    '3': '960th',
    '4': '860th',
    'Answer': '4'
  }


def db_print_question(q):
  for k in db[q]:
    if not k == 'Answer':
      print(f"{k}: {db[q][k]}")
  return db[q]["Answer"]


def db_ask_question(q):
  answer = db_print_question(q)
  guess = input('-->')
  if guess == answer:
    print("That's Right!!!")
# load_db()

# ____
# Local Dict
# ____
# unit_question = {1: {'Question 1': "Who is the 55th CBCS Commander",
#                      '1': 'Col. Garrison',
#                      '2': 'Lt. Col. Williams',
#                      '3': 'Maj. Spikes',
#                      '4': 'Capt. Ifan',
#                      'Answer': '2'},
#                  2: {'Question 2': 'What is our Group?',
#                      '1': '338th',
#                      '2': '336th',
#                      '3': '960th',
#                      '4': '860th',
#                      'Answer': '4'}

#                  }


# def print_question(q):
#     Q = unit_question[q]
#     for i, j in Q.items():
#         if not i == 'Answer':
#             print(i + ': ' + j)
#     return Q['Answer']


# def ask_question(q):
#     answer = print_question(q)
#     guess = input('-->')
#     if guess == answer:
#         print("That's Right!!!")


def dumpster():

  #here we set the secret. You can select any word to play with.
  word = ("FLY FIGHT WIN")

  #creates an variable with an empty value
  guesses = ''

  #determine the number of turns
  turns = 5

  # Create a while loop

  #check if the turns are more than zero
  while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

      # see if the character is in the players guess
      if char in guesses.upper():

        # print then out the character
        print(char, end=""),
      elif char == ' ':
        print(char)
      else:

        # if not found, print a dash

        print("_", end="")

        # and increase the failed counter with one
        failed += 1

    # if failed is equal to zero

    # print You Won
    if failed == 0:
      print("You won")
      # exit the script
      break
    # ask the user go guess a character
    guess = input("\nguess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess.upper() not in word:

      # turns counter decreases with 1 (now 9)
      turns -= 1

      # print wrong
      print("Wrong")

      # how many turns are left
      print("You have", +turns, 'more guesses')

      # if the turns are equal to zero
      if turns == 0:

        # print "You Lose"
        print("You Lose")


# dumpster()