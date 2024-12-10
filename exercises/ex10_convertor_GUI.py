import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet: ")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches: ")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_result = sg.Text(key="result")

layout1 = [[label_feet, input_feet],
          [label_inches, input_inches],
          [convert_button, exit_button, output_result]]

window = sg.Window("Convertor", layout=layout1)

while True:
    event, values = window.read()
    match event:
        case "Convert":
            feet_val = float(values['feet'])
            inches_val = float(values['inches'])
            result_val = feet_val * 0.3048 + inches_val* 0.0254
            window["result"].update(value=str(result_val)+" m")
        case "Exit":
            exit()
        case sg.WIN_CLOSED:
            break

window.close()