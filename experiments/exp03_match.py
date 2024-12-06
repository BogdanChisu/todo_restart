user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display": # bitwise OR operator
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case _: # convention is to use an underscore symbol
            print("Hey, you entered an unknown command")

print("Bye!")