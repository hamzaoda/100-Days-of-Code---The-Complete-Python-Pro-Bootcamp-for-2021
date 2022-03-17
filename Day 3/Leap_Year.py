syear = int(input("Please Enter THe Year : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"This year: {year}  is a Leap Year")
        else:
            print(f"This year: {year} is not a Leap Year")
    else:
        print(f"This year: {year}  is a Leap Year")
else:
    print(f"This year: {year} is not a Leap Year")
        