import random


word_list=["ardvark","baboon","camel"]
word = random.choice(word_list)
print(word)

guessed_letter=input("Please Enter a Letter : ").lower()
for letter in word:
    if letter == guessed_letter:
        print("Right")
    else:
        print("Wrong")