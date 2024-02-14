import re
from math import lcm

with open('input_part_2.txt') as file:
    lines = file.readlines()
    
    instructions = [int(char.replace('L', '0').replace('R', '1')) for char in lines[0].strip()]
    # print(instructions)
    
    nodes = {}
    for line in lines[2:]:
        nodes[line[0:3]]= [line[7:10],line[12:15]]
    # print(nodes)
    
    current = [k for k in nodes.keys() if re.match(r'..A', k)]
    ends = [k for k in nodes.keys() if re.match(r'..Z', k)]
    print(current)
    print(ends)

    needed_steps1 = []
    needed_steps2 = []
    for i, k in enumerate(current):
        steps = 0
        while k not in ends:
            k = nodes[k][instructions[steps%len(instructions)]]
            steps += 1
        needed_steps1.append(steps)
        first = k
        print(f"1st STOP NODE: {steps} needed to reach {k} from {current[i]}")

        # Finding the second stop node and its steps
        k = nodes[k][instructions[steps%len(instructions)]] 
        steps += 1
        while k not in ends:
            k = nodes[k][instructions[steps%len(instructions)]]
            steps += 1
        needed_steps2.append(steps)
        print(f"2nd STOP NODE: {steps} needed to reach {k} from {current[i]}")
        print(f"First stop steps / second stop steps = {needed_steps1[i] / needed_steps2[i]}")
        
        if k == first:
            print(f"first stop node = second stop node\n")
    # print(needed_steps1)
    # print(needed_steps2)
            
    # now let's find the least common multiple of all these periods
    current = needed_steps1[0]
    for i in range(len(needed_steps1)-1):
        current = lcm(current, needed_steps1[i+1])
    print(current)
