with open('input.txt') as file:
    lines = file.readlines()
    instructions = [char.replace('L', '0').replace('R', '1') for char in lines[0].strip()]
    instructions = [int(char) for char in instructions]
    # print(instructions)
    nodes = {}
    for line in lines[2:]:
        nodes[line[0:3]]= [line[7:10],line[12:15]]
    # print(nodes)
   
    k = 'AAA'
    steps = 0
    
    while k != 'ZZZ':
        k = nodes[k][instructions[steps%len(instructions)]]
        # print(k)
        steps += 1
    print(steps)



    