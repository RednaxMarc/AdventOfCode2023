#! /usr/bin/python3

# Max amount of blocks
max = {'red': 12, 'green': 13, 'blue': 14}
impossibleGames = []

# Open the file in read mode
file_path = 'D:\Documents\Howest\Linux\SF\Fedora\AdventOfCode2023\Day2\input.txt'

# Read each line of the file
with open(file_path, 'r') as file:
    for game, line in enumerate(file.readlines()):
        game = game + 1
        line = line.strip()
        # Split the line on colon and semi-colon
        line = line.split(':')
        line = line[1].split(';')
        print(line)
        # Check if the amount of blocks is correct
        for elem in line:
            for elem2 in elem.split(','):
                elem2 = elem2.strip()
                elem2 = elem2.split(' ')
                if int(elem2[0]) > max[elem2[1]]:
                    impossibleGames.append(game)
impossibleGames = set(impossibleGames)
impossibleGames = list(impossibleGames)
print(impossibleGames)
possibleGames = [num for num in range(1, 101) if num not in impossibleGames]
print(possibleGames)
print(sum(possibleGames))


        

            


 



        

    



