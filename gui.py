import functions
import FreeSimpleGUI as sg

label  = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
# each list in the layout list represents a row in the window

while True:
    event, values = window.read()
    print("Event ", event)
    print("Values", values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()