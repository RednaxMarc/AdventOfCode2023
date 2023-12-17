#!/usr/bin/python3

# Open the file in read mode
file_path = 'D:\Documents\Howest\Linux\SF\Fedora\AdventOfCode2023\Day3\input.txt'

# Read each line of the file
with open(file_path, 'r') as file:
    for line in file.readlines():
        # Strip the line of whitespace
        line = line.strip()
        print(line)