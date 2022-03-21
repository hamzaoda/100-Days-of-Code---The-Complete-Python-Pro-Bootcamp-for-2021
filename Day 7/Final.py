import random
import Hangman_Words
import Hangman_logos


stages = Hangman_logos.stages
number_of_lives=len(stages)
word = random.choice(Hangman_Words.word_list)
print(word)
empty_list =[]
for i in range(len(word)):
    empty_list.append('_')

choosen_word=[]
for letter in word:
    choosen_word.append(letter)

while '_' in empty_list and number_of_lives > 0:
    guessed_letter = input("Please Enter a Letter : ").lower()
    if guessed_letter not in empty_list:
        for letter in range(len(choosen_word)):
            if choosen_word[letter] == guessed_letter:
                empty_list[letter]= choosen_word[letter]
        if guessed_letter not in choosen_word:       
            number_of_lives -=1
            print(stages[number_of_lives])
            print(f"you lost a live the remaining lives is {number_of_lives}")
    else :
        print(f"you already have guessed {guessed_letter}")
    print(empty_list)
if number_of_lives == 0:
    print("You Lose")
else:
    print("You Win")