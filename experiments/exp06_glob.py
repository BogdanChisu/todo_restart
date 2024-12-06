import glob

myfiles = glob.glob("files/*.txt")
# get a list of all text files in the specified location

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())