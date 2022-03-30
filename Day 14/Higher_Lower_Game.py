import random
import game_data
import art


def checkAnswer(A, B):
    if A['follower_count'] > B['follower_count']:
        return A
    else:
        return B

def trnasformAnswer(user_answer, A, B):
    if user_answer == 'a':
        return A
    else:
        return B

print("Welcome to My Higher Lower Game!!")
print(art.logo)

data=game_data.data
answers=[]
answer = True
A=random.choice(data)
B=random.choice(data)
while answer:
    while A == B:
        B=random.choice(data)
    print(f"A : {A['name']}, {A['description']}, {A['country']}")
    print(art.vs)
    print(f"B : {B['name']}, {B['description']}, {B['country']}")
    correct_answer= checkAnswer(A, B)
    user_answer=input("Who Do You Think Have More Followers 'A' or 'B' : ").lower()
    user_answer=trnasformAnswer(user_answer, A, B)
    if correct_answer == user_answer:
        answers.append(B)
        A=correct_answer
        B=random.choice(data)
        while A == B and B in answers:

            if len(answers) == len(data):
                answer=False
                score=len(answers)
                print("You Finished all the questions good job")
                print(f"Your Score is {score}")
            else:
                B=random.choice(data)
                if B in answers:
                    print("-----------------------------------------")
                    print(B)
                    print("--------------------------------")
    else:
        answer = False
        score=len(answers)
        print("You Have Lost !! 😥😥")
        print(f"Your Score is {score}")

        
        

