import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice=int(input("what is your choice? 0 for Rock, 1 for Paper, 2 for scissors :"))
computer_choice=random.randint(0,2)
if user_choice == 0:
    print(f"You Choosed\n {game_images[user_choice]}")
    if computer_choice == 0:
        print(f"Computer Choose{game_images[computer_choice]}")
        print("it's Draw ")
    elif computer_choice == 1:
        print(f"Computer Choose{game_images[computer_choice]}")
        print("You Have Lost :(")
    else :
        print(f"Computer Choose{game_images[computer_choice]}")
        print("You Have Win! :)")
elif user_choice == 1:
    print(f"You Choosed\n {game_images[user_choice]}")
    if computer_choice == 0:
        print(f"Computer Choose{game_images[computer_choice]}")
        print("You Have Win! :)")
    elif computer_choice == 1:
        print(f"Computer Choose{game_images[computer_choice]}")
        print("it's Draw ")
    else :
        print(f"Computer Choose{game_images[computer_choice]}")
        print("You Have Lost :(")
else:
    print(f"You Choosed\n {game_images[user_choice]}")
    if computer_choice == 0:
        print(f"Computer Choose{game_images[computer_choice]}")
        print("You Have Lost :(")
    elif computer_choice == 1:
        print(f"Computer Choose{game_images[computer_choice]}")
        print("You Have Win! :)")
    else :
        print(f"Computer Choose{game_images[computer_choice]}")
        print("it's Draw ")
        
    
