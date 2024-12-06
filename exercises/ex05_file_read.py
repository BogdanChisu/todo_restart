filenames = ["a.txt", "b.txt", "c.txt"]

for file in filenames:
    reader = open(file, "r")
    content = reader.read()
    print(content)
    reader.close()