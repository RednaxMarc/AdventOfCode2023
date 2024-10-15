import numpy as np

## Read in the file
with open("test1.txt") as file:
    data = np.array([list(line.strip()) for line in file])
    print(data[1,1])
    
    # Find the "S" in the data
    start = np.where(data == "S")
    print(start)
    print(data[start])

    ## Define the directions
    # "|": up or down, so y +1  or y -1
    # "-": left or right, so x +1 or x -1
    # "L": down and right, so y +1 and x +1, or left and up, so x -1 and y -1
    # "J": down and left, so y +1 and x -1, or right and up, so x +1 and y -1
    # "7": up and left, so y -1 and x -1, or right and down, so x +1 and y +1
    # "F": up and right, so y -1 and x +1, or left and down, so x -1 and y +1
    # ".": no movement
    # "S": start

    



    




    
