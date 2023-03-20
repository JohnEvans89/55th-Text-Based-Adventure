import os
# nnn


def straight_line():
  os.system("clear")
  prCyan("―" * 30)
  prRed(" * " * 10)
  prCyan("―" * 30)


def press_enter():
  input("\n*** Press Enter ***\n")


def prCyan(skk):
  print("\033[96m{}\033[00m".format(skk))


def prRed(skk):
  print("\033[91m{}\033[00m".format(skk))
