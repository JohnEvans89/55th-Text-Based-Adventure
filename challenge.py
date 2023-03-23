# # this will be the dumpster challenge
# # you will need to crack the code
# # A=1, etc. with coded answer
# # 3 attempts win gets key. Lose, you don't get the key and challenge locks

# # sorta like a hangman game structure
# # 3 ways to do it
# # -have a dictionary of alphabet and the puzzle and check if the guess matches the puzzle
# #  /alphabet pair. Return correct letter
# # -have them solve the puzzle totally and return a true/False
# # -have the guess and fill in what was right
# alphabet={1:'A',2:'B',5:'L'}

# puzzle=['A']
# print(alphabet[1])

# puzzle_2='N______ C__ S___\nT__ U_ A__ F___'
# puzzle_2_answer='NOTHING CAN STOP\nTHE U.S. AIR FORCE'
# print(puzzle_2)
# print('H'in puzzle_2_answer)

# #wait for 1 second
# time.sleep(1)

# print("Start guessing...")
# time.sleep(0.5)
#importing the time module
import time


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


dumpster()
