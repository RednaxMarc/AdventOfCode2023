import re

with open('input_part_2.txt') as file:
    lines = file.readlines()
    
    instructions = [int(char.replace('L', '0').replace('R', '1')) for char in lines[0].strip()]
    print(instructions)
    
    nodes = {}
    for line in lines[2:]:
        nodes[line[0:3]]= [line[7:10],line[12:15]]
    print(nodes)

    current = [k for k in nodes.keys() if re.match(r'..A', k)]
    ends = [k for k in nodes.keys() if re.match(r'..Z', k)]
    print(current)
    print(ends)
    
    steps = 0
    
    