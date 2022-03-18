import random

test_seed=int(input("Create a seed number : "))
random.seed(test_seed)

outcome =random.randint(1, 2)
if outcome == 1:
    print("Heads")
else :
    print("Tails")