from random import randrange

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
selection_number = randrange(lower_bound, upper_bound)

print(selection_number)