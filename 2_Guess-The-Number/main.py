import random

def guess(max_number):
    random_number = random.randint(1, max_number)

    while True:
        user_guessing = input("Guess: ")
        if int(user_guessing) > random_number:
            print("Try a lower number!")
        elif int(user_guessing) < random_number:
            print("Try a higher number!")
        else:
            break

    print("\n"
          "===========================================================\n"
          f"         Congrats! You have guessed the number {random_number}          \n"
          "===========================================================")




print(
'''
____ _  _ ____ ____ ____    ___ _  _ ____    _  _ _  _ _  _ ___  ____ ____ 
| __ |  | |___ [__  [__      |  |__| |___    |\ | |  | |\/| |__] |___ |__/ 
|__] |__| |___ ___] ___]     |  |  | |___    | \| |__| |  | |__] |___ |  \ 
'''
)
print("")
max_number = int(input("Choose the maximum number: "))
guess(max_number)

