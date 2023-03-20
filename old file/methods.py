# def press_enter_method(text):
#     print("")
#     choice = input("\nEnter to continue...")
#
#     if not choice == '' or choice == "":
#         clear()
#         return text()


def description_press_enter(description):
  print(description)
  choice = input("\nEnter to continue...")


def description_press_enter_method(*args):
  print(args[0])
  choice = input("\nEnter to continue...")
  if len(args) > 2:
    if not choice == '' or choice == "":
      return (args[1](args[2], args[3], args[4], args[5]))
  else:
    if not choice == '' or choice == "":
      clear()
      args[1]()


def heading(message):
  print('-' * 20)
  print(message)
  print('-' * 20)


def clear():
  print("\n" * 10)


def print_separator(n):
  print("-" * n)


def print_heading(title):
  print_separator(30)
  print(title)
  print_separator(30)


def prompt():
  choice = input('-->')
  return choice
