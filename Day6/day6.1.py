# Problem 1
with open('input.txt') as file: 
    lines = file.readlines()
    times = [int(x) for x in lines[0].strip().split(' ')[1:] if x!='']
    distances = [int(x) for x in lines[1].strip().split(' ')[1:] if x!='']
    print(times)
    print(distances)

    possibilites = 1
    for i, time in enumerate(times):
        distance = distances[i]
        wins=0
        for j in range(1, time+1):
            d = (time-j)*j
            if d > distance:
                wins+=1
        possibilites *= wins
    print(possibilites)
file.close()
    