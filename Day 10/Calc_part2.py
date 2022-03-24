





#Calculate

#Add
def add(n1, n2):
    return n1 + n2

#Sub
def sub(n1, n2):
    return n1 - n2
#Mul
def mul(n1, n2):
    return n1 * n2

#Div
def div(n1, n2):
    return n1 / n2 


operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

num1=int(input("Please Enter The First Number : "))


for operator in operators:
    print(operator)
operator_symbol =input("Please Enter one of the operators : ")
num2=int(input("Please Enter The Second Number : "))
function = operators[operator_symbol]
answer = function(num1, num2)


print(f"{num1} {operator_symbol} {num2} = {answer}")

keep = True
y_or_n = input(f"Please Enter 'y' to go with {answer} or 'n' to exit : ")
if y_or_n == 'n':
    keep = False
while keep:
    for operator in operators:
        print(operator)
    operator_symbol =input("Please Enter one of the operators : ")
    new_num = int(input("Please Enter Please Enter a new number : "))
    function = operators[operator_symbol]
    old_answer= answer
    answer = function(answer, new_num)
    print(f"{old_answer} {operator_symbol} {new_num} = {answer}")
    y_or_n = input(f"Please Enter 'y' to go with {answer} or 'n' to exit : ")
    if y_or_n == 'n':
        keep = False
        