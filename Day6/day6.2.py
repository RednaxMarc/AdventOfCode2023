# Problem 2
with open('input.txt') as file: 
    lines = file.readlines()
    time = int(''.join([x for x in lines[0].strip().split(' ')[1:] if x!='']))
    distance = int(''.join([x for x in lines[1].strip().split(' ')[1:] if x!='']))
    print(time)
    print(distance)
    wins = 0
    for j in range(1, time+1):
        d = (time-j)*j
        if d > distance:
            wins+=1
    print(wins)