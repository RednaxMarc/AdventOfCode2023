# Read in the file
with open("test2.txt") as file:
    # Find the x and y coordinate of the "S" in the file
    for y, line in enumerate(file):
        if "S" in line:
            x = line.index("S")
            print(x, y)
