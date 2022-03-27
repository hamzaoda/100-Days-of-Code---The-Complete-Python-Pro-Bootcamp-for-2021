import random

ATTEMPTS = 0

print("Welcome To The Guessing Game!!!")
print("I'm Thinking of a Number between 1 and 100!!!")
dif=input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
while dif != 'easy' and dif != 'hard':
    dif = input("Please Choose a difficulty. Type 'easy' or 'hard' : ").lower()
if dif == "easy":
    ATTEMPTS = 10
else:
    ATTEMPTS = 5
number = random.randint(1, 10)
print(f"You Have {ATTEMPTS} Attempts Remaining To Guess The Nummber")
guessed_nummber = 0
while number != guessed_nummber and ATTEMPTS !=0:
    guessed_nummber = int(input("Make a guess : "))
    if guessed_nummber == number:
        print("You Have win !!")
    elif guessed_nummber > number:
        print("To High !!")
        print("Guess again")
        ATTEMPTS -=1
        print(f"You Have {ATTEMPTS} Attempts Remaining To Guess The Nummber")
    else:
        print("To Low !!")
        print("Guess again")
        ATTEMPTS -=1
        print(f"You Have {ATTEMPTS} Attempts Remaining To Guess The Nummber")
if ATTEMPTS == 0:
    print("You have lost :(")

