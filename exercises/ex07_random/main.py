from parsers import parse
import random

# Ask the user to enter a lower and upper bound divided by a comma
user_input = input("Enter a lower bound and an upper bound divided by a "
                   "comma (e.g., 2, 10)")

parsed = parse(user_input)

# Pick a randon int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)