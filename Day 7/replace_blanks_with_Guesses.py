import random


word_list=["ardvark","baboon","camel"]
word = random.choice(word_list)
print(word)
empty_list =[]
for i in range(len(word)):
    empty_list.append('_')


guessed_letter=input("Please Enter a Letter : ").lower()

choosen_word=[]
for letter in word:
    choosen_word.append(letter)
print(choosen_word)

for letter in range(len(choosen_word)):
    if choosen_word[letter] == guessed_letter:
        empty_list[letter]= choosen_word[letter]
    else:
        print("Wrong")
print(empty_list)