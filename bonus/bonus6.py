contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced",
            "The slicing process wass well presented"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(contents, filenames):
    file = open(f"../files/{filenames}", "w")
    # files folder had to be located first
    file.write(content)
    file.close()