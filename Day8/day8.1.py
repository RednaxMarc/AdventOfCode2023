import re

with open('test.txt') as file:
    lines = file.readlines()
    instructions = [char.replace('L', '0').replace('R', '1') for char in lines[0].strip()]
    print(instructions)
    nodes = {}
    for line in lines[2:]:
        nodes[line[0:3]]= [line[7:10],line[12:15]]
    print(nodes)
   
    k = 'AAA'
    steps = 0
    
    for i in instructions:
        while k != 'ZZZ':
            print(k)
            k = nodes[k][int(i)]



    