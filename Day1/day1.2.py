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
firstDigit = []
lastDigit = []
file_path = 'input.txt'
with open(file_path, 'r') as file:
    # Read each line and append it to the list
    for line in file: 
        line = line.strip()
        found = False
        for i in range(len(line)):
            if line[i].isdigit():
                firstDigit.append(line[i])
                found = True
                break
            for k, v in number_dict.items():
                if line[i:].startswith(k):
                    firstDigit.append(v)
                    found = True
                    break
            if found:
                break
        found = False
        for i in range(len(line)-1 , -1, -1):
            if line[i].isdigit():
                lastDigit.append(line[i])
                found = True
                break
            for k, v in number_dict.items():
                if line[i:].startswith(k):
                    lastDigit.append(v)
                    found = True
                    break
            if found:
                break

    # print(firstDigit)
    # print(lastDigit)
    stringResult = [str(item1) + str(item2) for item1, item2 in zip(firstDigit, lastDigit)]
    # Convert everything to an integer
    finalResult = []
    for i in stringResult:
        i = int(i)
        finalResult.append(i)

    # Sum it up
    sum = sum(finalResult)
    print(sum)