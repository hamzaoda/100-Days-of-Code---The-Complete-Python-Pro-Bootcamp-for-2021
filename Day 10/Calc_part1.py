





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
num2=int(input("Please Enter The Second Number : "))

for operator in operators:
    print(operator)
operator_symbol =input("Please Enter one of the operators : ")

function = operators[operator_symbol]
answer = function(num1, num2)


print(f"{num1} {operator_symbol} {num2} = {answer}")