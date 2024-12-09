import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet: ")
input_feet = sg.InputText()

label_inches = sg.Text("Enter inches: ")
input_inches = sg.InputText("")

convert_button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[label_feet, input_feet],
                           [label_inches, input_inches],
                           [convert_button]])

window.read()
window.close()