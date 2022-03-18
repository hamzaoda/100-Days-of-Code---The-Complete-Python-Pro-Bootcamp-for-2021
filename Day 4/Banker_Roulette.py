import random

test_seed=int(input("Create a seed number : "))
random.seed(test_seed)

namesAsCsv= input("Give me Everybody Name separated by commas : ")
names = namesAsCsv.split(", ")

print(random.choice(names))