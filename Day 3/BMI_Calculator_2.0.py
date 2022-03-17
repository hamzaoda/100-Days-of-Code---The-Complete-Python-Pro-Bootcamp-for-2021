height= float(input("Please Enter your height :"))
weight = int(input("Please Enter your weight :"))

BMI = weight / height ** 2
BMI = round(BMI, 2)
if BMI <18.5 :
    print(f"your BMI is {BMI} and you are underweight")
elif BMI <25:
    print(f"your BMI is {BMI} and you are normalweight")
elif BMI <30:
    print(f"your BMI is {BMI} and you are overweight")
elif BMI <35:
    print(f"your BMI is {BMI} and you are obese")
else :
    print(f"your BMI is {BMI} and you are clinically obse")