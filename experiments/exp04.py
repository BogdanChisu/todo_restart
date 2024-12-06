user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            print(f"Length is {len(todos)}")
            # variables exist outside of the loop because they were defined
            # on the for level
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number -= 1
            todo_to_edit = todos[number]
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case "exit":
            break

print("Bye!")