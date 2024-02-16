sum = 0
with open("input.txt") as file:
    for line in file.readlines():
        values = {}
        values[0] = [int(x) for x in line.strip().split(" ")]
        # print(values)

        # Using a loop to calculate the differences between the values until they are all equal
        n = 1
        are_all_equal = False
        while are_all_equal == False:
            values[n] = [values[n-1][i] - values[n-1][i-1] for i in range(1, len(values[n-1]))]
            are_all_equal = all(x == values[n][0] for x in values[n][1:])
            n += 1
        # print(values)
            
        # Duplicate the a value of the last key:value pair
        values[len(values)-1].append(values[len(values)-1][-1])
        # print(values)

        # Extrapolating like the example online
        for x in range(len(values)-1 , 0, -1):
            values[x-1].insert(0, values[x-1][0] - values[x][0])
        print(values)
        sum += values[0][0]
    print(sum)