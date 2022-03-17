print("Welcome to the love Calculator")
name1= input("Please Enter The your Name : ")
name2= input("Please Enter The thier Name : ")

name1 =name1.lower()
name2 =name2.lower()
T=name2.count('t') + name1.count('t')
R=name2.count('r') + name1.count('r')
U=name2.count('u') + name1.count('u')
E=name2.count('e') + name1.count('e')

L=name2.count('l') + name1.count('l')
O=name2.count('o') + name1.count('o')
V=name2.count('v') + name1.count('v')

true=T+R+U+E
love=L+O+V+E
true_love=str(true) + str(love)
true_love_percentage = int(true_love)
if true_love_percentage < 10 or true_love_percentage > 90 :
    print(f"Your Score is {true_love}, You Go Togther Like Coke And Mentos")
elif true_love_percentage > 40 and true_love_percentage < 50:
    print(f"Your Score is {true_love}, You Are Alright Togther")
else:
    print(f"Your Score is {true_love}")
