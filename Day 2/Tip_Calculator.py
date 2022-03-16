total_bill = float(input("Please Enter the total_bill : "))
tip_percentage = int(input("Please Enter the percentage you would like to give 10, 12, 15 : "))
number_of_people= int(input("Please Enter the numnber of people who will pay : "))
pay = round((total_bill + (total_bill * tip_percentage/100)) / number_of_people, 2)
print(f"Each person should pay : {pay}")

