password = input("Enter a new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

for i in password:
    if i.isdigit():
        result["digit"] = True
        break

for i in password:
    if i.isupper():
        result["uppercase"] = True
        break

# print(result)
# print(all(result)) # checks the members of the list and if one of them if
# False it returns False

print(result)
print(result.values())

if all(result.values()) == True:
    print("Strong Password")
else:
    print("Weak Password")