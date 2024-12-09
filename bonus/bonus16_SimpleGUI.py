import FreeSimpleGUI as sg

# line1
label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

# line2
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FilesBrowse("Choose")

# window
compress_button = sg.Button("Compress")
window = sg.Window("File compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

window.read()
window.close()