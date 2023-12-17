#! /usr/bin/python3
import re
# Open the file in read mode
file_path = 'D:\Documents\Howest\Linux\SF\Fedora\AdventOfCode2023\Day2\input.txt'

products = []

# Read each line of the file
with open(file_path, 'r') as file:
    for line in file.readlines():
        line = line.strip()

        # Split the line on colon and semi-colon
        line = line.split(':')
        line = line[1].split(';')
        print(line)

        red = []
        green = []
        blue = []

        # Check the lowest amount of blocks per color
        for elem in line:
            for elem2 in elem.split(','):
                elem2 = elem2.strip()
                elem2 = elem2.split(' ')
                if elem2[1] == 'red':
                    red.append(int(elem2[0]))
                elif elem2[1] == 'green':
                    green.append(int(elem2[0]))
                elif elem2[1] == 'blue':
                    blue.append(int(elem2[0]))
        maxRed = max(red)
        maxGreen = max(green)
        maxBlue = max(blue)
        product = maxRed * maxGreen * maxBlue
        products.append(product)
print(products)
print(sum(products))
            

        

            


 



        

    



