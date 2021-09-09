import random


def play_game():
    print("What's you choice? 'r' for Rock, 'p' for paper or 's' for scissors")
    feedback = input("Your choice: ")
    cpu_choice = random.randint(0, 2)

    choices = ['r', 'p', 's']
    cpu_choice = choices[cpu_choice]

    result(feedback, cpu_choice)


def result(feedback, cpu_choice):
    if feedback == cpu_choice:
        print("It's a draw!")
    elif feedback == 'r':
        if cpu_choice == 'p':
            you_won()
        else:
            you_lost()

    elif feedback == 'p':
        if cpu_choice == 'r':
            you_won()
        else:
            you_lost()

    elif feedback == 's':
        if cpu_choice == 'p':
            you_won()
        else:
            you_lost()


def you_won():
    print("You won!")


def you_lost():
    print("You lost!")


play_game()
