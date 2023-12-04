# Open the file in read mode
file_path = '/media/sf_SF/Fedora/AdventOfCode2023/Day1/input.txt'  # Replace this with the path to your file
lines_list = []

with open(file_path, 'r') as file:
    # Read each line and append it to the list
    for line in file:
        lines_list.append(line.strip())  # Use strip() to remove trailing newline characters or extra spaces

stringNum = []
revstringNum = []
intNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for string in lines_list: # Check for the first number in the string and add it to a list
    for i in string:
        if i in intNumbers:
            stringNum.append(i)
            break
    for i in string[::-1]: # Check for the last number in the sting and add it to a list
        if i in intNumbers:
            revstringNum.append(i)
            break

# Zip the two lists and concatenate their values
stringResult = [str(item1) + str(item2) for item1, item2 in zip(stringNum, revstringNum)]

# Convert everything to an integer
finalResult = []
for i in stringResult:
    i = int(i)
    finalResult.append(i)

# Sum it up
sum = sum(finalResult)
print(sum)



    

    