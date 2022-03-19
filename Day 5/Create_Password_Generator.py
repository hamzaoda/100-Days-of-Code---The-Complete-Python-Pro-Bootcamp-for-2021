import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '%', '$' , '&', '^', '*' , '(' , ')' , '-', '+']

print("Welcome to My Password Generator !")
number_of_letters = int(input('Enter the number of letters please : \n'))
number_of_numbers = int(input("Please Enter The number of numbers : \n"))
number_of_symbols = int(input("Plese Enter The number of symbols : \n"))

letter=''
for i in range(number_of_letters):
    letter += random.choice(letters)
    
number=''
for j in range(number_of_numbers):
    number += random.choice(numbers)

symbol=''
for k in range(number_of_symbols):
    symbol += random.choice(symbols)

the_generated_password = letter+number+symbol
password_list= []
for i in the_generated_password:
    password_list.append(i)
random.shuffle(password_list)

password=""
for i in password_list:
    password += i
    
print(f"the generated password is : {password}")
