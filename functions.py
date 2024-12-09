FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items. """
    with open(filepath, "r") as file:
        tasks = file.readlines()
    return tasks


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a todo items list in a text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
        # functions that don't have a return statement will return the None
        # value

print(__name__)

if __name__ == "__main__":
    # this is how you control what code is run when you run the script
    # directly or indirectly by importing it
    # this lines are executed only when the file is executed directly
    print("Hello")
    print(get_todos())