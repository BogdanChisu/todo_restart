from bonus.converters14 import convert
from bonus.parser14 import parse

feet_inches = input("Enter feet and inches: ")

f, i = parse(feet_inches)
print("fi", f, i)
result = convert(f, i)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")