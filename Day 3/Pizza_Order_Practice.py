print("Welcome to Python Deliveries! ")
size = str.lower(input("Please Enter The Size of The Pizza :"))
add_pepperoni = input("Do You Want Pepperoni : ")
extra_cheese = input("Do You Want extra Cheese :")

bill = 0
if size == 's':
    bill +=15
    if add_pepperoni == 'y':
        bill +=2
elif size == 'm':
    bill +=20
    if add_pepperoni == 'y':
        bill +=3
elif size == 'l':
    bill +=25
    if add_pepperoni == 'y':
        bill +=3
if extra_cheese == 'y':
    bill +=1
print(f"your total bill is : ${bill}")
