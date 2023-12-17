#!/usr/bin/python3

# Define input file path
file_path = 'D:\Documents\Howest\Linux\SF\Fedora\AdventOfCode2023\Day4\input.txt'

scores = []

# Read each line of the file
with open(file_path, 'r') as file:
    for line in file.readlines():
        line = line.strip()
        line = line.split(':')[1]
        line = line.split('|')

        lotteryList = []
        matches = 0
        
        # Split each line into a list of numbers and append to lotteryList
        for elem in line:
            elem = elem.strip()
            elem = elem.split(' ')
            elem = [number for number in elem if number != '']
            lotteryList.append(elem)
        
        print(lotteryList)
        
        for number in lotteryList[0]:
            if number in lotteryList[1]:
                matches += 1
        if matches != 0:
            score = 2 ** (matches-1)
        else:
            score = 0
        scores.append(score)
        print(matches)
        print(score)
    print(scores)
    print(sum(scores))
                
                