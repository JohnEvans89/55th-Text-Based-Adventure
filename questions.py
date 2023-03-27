unit_question = {1: {'Question 1': "Who is the 55th CBCS Commander",
                     '1': 'Col. Garrison',
                     '2': 'Lt. Col. Williams',
                     '3': 'Maj. Spikes',
                     '4': 'Capt. Ifan',
                     'Answer': '2'},
                 2: {'Question 2': 'What is our Group?',
                     '1': '338th',
                     '2': '336th',
                     '3': '960th',
                     '4': '860th',
                     'Answer': '4'}

                 }


def print_question(q):
    Q = unit_question[q]
    for i, j in Q.items():
        if not i == 'Answer':
            print(i + ': ' + j)
    return Q['Answer']


def ask_question(q):
    answer = print_question(q)
    guess = input('-->')
    if guess == answer:
        print("That's Right!!!")



# ask_question(2)
