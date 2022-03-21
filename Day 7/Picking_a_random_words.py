import random


word_list=["ardvark","baboon","camel"]
word = random.choice(word_list)

guessed_letter=input("Please Enter a Letter : ")
for letter in word:
    if letter == guessed_letter:
        print("Right")
    else:
        print("Wrong")