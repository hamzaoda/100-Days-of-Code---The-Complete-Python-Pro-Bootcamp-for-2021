from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()


should_continue =True


while should_continue:
    choice = input(f"What Would You like? ({menu.get_items()}) ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        should_continue = False
    else:
        choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
                
                    
        
        