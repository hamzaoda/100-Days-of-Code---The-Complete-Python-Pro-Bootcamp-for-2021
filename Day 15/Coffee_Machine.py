import Resources

menu = Resources.MENU
resources = Resources.resources

def printReport():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${resources['money']}")


def checkResources(answer):
    for ingredient in answer['ingredients']:
        if resources[ingredient] < answer['ingredients'][ingredient]:
            return False, ingredient
    return True, None


def ProcessCoins():
    print("Please Insert Coins.")
    quarters = int(input("How Many Quarters? : "))
    dimes = int(input("How Many Dimes? : "))
    nickles = int(input("How Many Nickles? : "))
    pennies = int(input("How Many Pennies? : "))
    coins = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
    return coins      


def checkTransaction(money, answer):
    if money < answer['cost']:
        return False
    return True


def makeRequest(inserted_amount, answer):
    for ingredient in answer['ingredients']:
        resources[ingredient] -= answer['ingredients'][ingredient]
    change = inserted_amount - answer['cost']
    return change
    


should_continue = True
while should_continue:
    request = input("What would you like (espresso/latte/cappuccino)? ").lower()
    if request == "report":
        printReport()
    elif request in menu:
        answer = menu[request]
        is_enough_resource, resource = checkResources(answer)
        if is_enough_resource:
            inserted_amount = ProcessCoins()
            is_enough_money = checkTransaction(inserted_amount, answer)
            if is_enough_money:
                change = makeRequest(inserted_amount, answer)
                print(f"Here is your {request} !!!")
                print(f"here is the change ${change}")  
            else:
                print("insufficient money\nplease try again")
        else:
            print(f"There is no enough {resource} for your drink")
            should_continue = False  
    elif request == "off":
        should_continue = False         
    else:
        print("Please Enter one of the drikns !")