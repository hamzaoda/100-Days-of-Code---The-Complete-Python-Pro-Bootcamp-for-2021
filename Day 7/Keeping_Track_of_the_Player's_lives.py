import random

stages=["stage6", "stage5", "stage4", "stage3", "stage2", "stage1"]
number_of_lives=len(stages)
print(number_of_lives)
word_list=["ardvark","baboon","camel"]
word = random.choice(word_list)
print(word)
empty_list =[]
for i in range(len(word)):
    empty_list.append('_')

choosen_word=[]
for letter in word:
    choosen_word.append(letter)

while '_' in empty_list and number_of_lives > 0:
    guessed_letter = input("Please Enter a Letter : ").lower()
    for letter in range(len(choosen_word)):
        if choosen_word[letter] == guessed_letter:
            empty_list[letter]= choosen_word[letter]
    if guessed_letter not in choosen_word:       
        number_of_lives -=1
        print(stages[number_of_lives])
    print(empty_list)
if number_of_lives == 0:
    print("You Lose")
else:
    print("You Win")