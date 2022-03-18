import random

row1=["😀", "😁", "😂"]
row2=["🤣", "😃", "😄"]
row3=["😅", "😆", "😉"]

map = [row1, row2, row3]
print(f" {row1}\n {row2}\n {row3}\n")
posistion= input("Where Do You Want To Put The Treasure : ")
column = int(posistion[0]) -1
row = int(posistion[1]) -1
# if row == 0:
#     row1[column]= 'X'
# elif row == 1:
#     row2[column]= 'X'
# else:
#     row3[column]= 'X'
map[row][column] = 'X'
print(f" {row1}\n {row2}\n {row3}\n")
