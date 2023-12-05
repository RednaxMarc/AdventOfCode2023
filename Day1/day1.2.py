import re

# Open the file in read mode
file_path = '/media/sf_SF/Fedora/AdventOfCode2023/Day1/input.txt'  # Replace this with the path to your file
lines_list = []

with open(file_path, 'r') as file:
    # Read each line and append it to the list
    for line in file:
        lines_list.append(line.strip())  # Use strip() to remove trailing newline characters or extra spaces

# Replacement dict
number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# Read the lines of the inputfile and search for the patterns
result = 0
for line in lines_list:
    digits = []
    matched_digits = re.findall("\d|one|two|three|four|five|six|seven|eight|nine",  line)
   
    # Take out the first and last match
    firstlast_digits = [matched_digits[0], matched_digits[-1]]
    
    # replace the words with numbers
    index = 0
    for number in firstlast_digits:
        if number in number_dict.keys():
            firstlast_digits[index] = number_dict[number]
        index += 1
    
    # stick the two numbers to each other
    firstlast_digits = firstlast_digits[0] + firstlast_digits[1]
    
    # convert them to integers
    firstlast_digits = int(firstlast_digits)
    print(firstlast_digits)
    #print(type(firstlast_digits))
    # sum up the integers
    result = result + firstlast_digits
print(result)
    

                 