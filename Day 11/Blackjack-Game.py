import random
import Logo


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def getCard():
    return random.choice(cards)
def addCardToUser():
    user_cards.append(getCard())
def addCardToComputer():
    computer_cards.append(getCard())
def sumOfCards(some_list):
    return sum(some_list)
def checkAce(score, some_list):
    if score > 21:
        if 11 in some_list:
            some_list.remove(11)
            some_list.append(1)
def checkWinner(user_score, computer_score):
    if user_score > 21:
        print("you Have Lost")
    elif computer_score > 21:
        print("you Have Win")
    elif user_score > computer_score :
        print("you have Win")
    elif computer_score > user_score :
        print("you have Lost")
    else:
        print("it's a Draw")
def printUserScore():
        print(f"your cards are : {user_cards} and your score is {user_score}")
def printComputerScore():
    print(f"the dealer Cards are : {computer_cards} and his score is {computer_score}")
def low(score, some_list):
    while score < 17 :
        some_list.append(getCard())
        score = sumOfCards(some_list)
        
    
user_score = 0
computer_score = 0
play = True    
answer = input("do you want to play 'y' for play and 'n' to exit : ")  
if answer == "n":
    play = False    
else:
    play = True  
while play:
    user_cards = []
    computer_cards = []
    print(Logo.logo)
    print("Welcome to My BlackJack Game!!!")
    addCardToUser() 
    addCardToUser()
    addCardToComputer()
    addCardToComputer()
    user_score= sumOfCards(user_cards)
    computer_score= sumOfCards(computer_cards)
    print(f"your cards are : {user_cards} and your score is {user_score}")
    print(f"the dealer first card is :{computer_cards[0]}")
    
    if (user_score == 21 or computer_score == 21) and (len(user_cards) == 2 or len(computer_cards) == 2):
        print("------------------------------")
        low(user_score, user_cards)
        low(computer_score, computer_cards)
        printUserScore()
        printComputerScore()
        checkWinner(user_score, computer_score)
        print("------------------------------")
    else:
        another=input("Please Enter a 'y' to get another card and 'n' to pass : ")
        if another == "y":
            addCardToUser()
            checkAce(user_score, user_cards)
            checkAce(computer_score, computer_cards)
            user_score= sumOfCards(user_cards)
            computer_score= sumOfCards(computer_cards)
            low(user_score, user_cards)
            low(computer_score, computer_cards)
            checkAce(user_score, user_cards)
            checkAce(computer_score, computer_cards)
            user_score= sumOfCards(user_cards)
            computer_score= sumOfCards(computer_cards)
            printUserScore()
            printComputerScore()
            checkWinner(user_score, computer_score)
        else:
            checkAce(user_score, user_cards)
            checkAce(computer_score, computer_cards)
            user_score= sumOfCards(user_cards)
            computer_score= sumOfCards(computer_cards)
            low(user_score, user_cards)
            low(computer_score, computer_cards)
            checkAce(user_score, user_cards)
            checkAce(computer_score, computer_cards)
            user_score= sumOfCards(user_cards)
            computer_score= sumOfCards(computer_cards)
            printUserScore()
            printComputerScore()
            checkWinner(user_score, computer_score)
        answer = input("do you want to play again 'y' for play and 'n' to exit : ")  
        if answer == "n":
            play = False    
        else:
            play = True
        
    
    