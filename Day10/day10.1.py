import numpy as np

## Read in the file
with open("test1.txt") as file:
    data = np.array([list(line.strip()) for line in file])
    print(data)
    
    # Find the "S" in the data
    start = np.where(data == "S")
    print(start)
    print(data[start])
    current = start

    ## Define the directions
    # "|": N, or opposite
    # "-": E, or opposite
    # "L": SE, or opposite
    # "J": SW, or opposite
    # "7": ES, or opposite
    # "F": NE, or opposite
    # ".": no movement
    # "S": start

    opposite = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E",
    }
    allowed_directions = 


    



    



    




    
