from replit import db

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
