import FreeSimpleGUI as sg

def km_to_files(km):
    return km / 1.6

label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")

layout = [[label, input_box], [miles_button, output]]
window = sg.Window("Km to Miles Converter", layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = float(values["kms"])
            result = km_to_files(km)
            window["output"].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()