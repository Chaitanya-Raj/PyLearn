import random


answers = ['yes', 'no', 'maybe', 'idk', 'YASS']


def question():
    ques = input("Ask a question : ")
    print(answers[random.randint(0, 4)])
    end()


def end():
    play = input('\nDo you want to ask another question? (y/n) : ')
    if play == 'y':
        question()


print("Welcome to the Magic 8 Ball !!!", end="\n\n")
question()
