import random


def computer_guess():
    answer = ' '
    print("The computer will try to guess a number chosen by YOU. \n"
          "However, you have to help it by entering either \nC (for correct) \n"
          "or L (for lower)\nor H (for higher)\n")

    min_number = int(input("Enter the lower boundary: "))
    max_number = int(input("Enter the higher boundary: "))
    feedback = ''

    while feedback != 'c' and feedback != 'C':
        guess = random.randint(min_number, max_number)
        feedback = input(f"I guessed the number {guess}. Is it too high (H), too low (L) or correct (C)? Your answer: ")
        if feedback == 'h' or feedback == 'H':
            max_number = guess - 1
        elif feedback == 'l' or feedback == 'L':
            min_number = guess + 1

    print(f"\nGood collaboration :)! The computer guessed your number, {guess}, correctly!")



print(
    '''
    ____ _  _ ____ ____ ____    ___ _  _ ____    _  _ _  _ _  _ ___  ____ ____          ____ _ 
    | __ |  | |___ [__  [__      |  |__| |___    |\ | |  | |\/| |__] |___ |__/    __    |__| | 
    |__] |__| |___ ___] ___]     |  |  | |___    | \| |__| |  | |__] |___ |  \          |  | | 
                                                                                               
    '''
)
computer_guess()
