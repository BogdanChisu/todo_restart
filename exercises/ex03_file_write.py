new_user = input("Add a new member: ")

file = open("members.txt", "r")

members_list = file.readlines()
file.close()

members_list.append(new_user + "\n")

file = open("members.txt", "w")
file.writelines(members_list)
file.close()