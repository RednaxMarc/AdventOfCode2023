# Open the file in read mode
file_path = '/media/sf_SF/Fedora/AdventOfCode2023/Day1/input.txt'  # Replace this with the path to your file
lines_list = []

with open(file_path, 'r') as file:
    # Read each line and append it to the list
    for line in file:
        lines_list.append(line.strip())  # Use strip() to remove trailing newline characters or extra spaces

stringNum = []
revstringNum = []
for string in lines_list: # Check for the first number and ad it to a list
    for i in string:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            stringNum.append(i)
            break
    for i in string[::-1]: # Check for the second number and ad it to a list
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            revstringNum.append(i)
            break

# Zip the two lists and concatenate their values
stringResult = [str(item1) + str(item2) for item1, item2 in zip(stringNum, revstringNum)]
print(stringResult)

# Convert everything to a integer
finalResult = []
for i in stringResult:
    i = int(i)
    finalResult.append(i)
print(finalResult)

# Sum it up
sum = sum(finalResult)
print(sum)



    

    