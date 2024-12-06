from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos, "files/todos.txt")


    elif user_action.startswith("show"):
        print("Show command issued")

        todos = get_todos()

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            print(new_todo)
            todos[number] = new_todo + "\n"
            print(todos)

            write_todos(todos, "files/todos.txt")

        except ValueError as error:
            print("Your selection is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos, "files/todos.txt")

            message = f"Todo <<{todo_to_remove}>> was removed from the list."
            print(message)

        except IndexError:
            print("There is no number with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print("Bye!")