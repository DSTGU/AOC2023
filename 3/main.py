schematic = open("input.txt").readlines()

print(schematic)
total = 0
gears = 0
legalgears = 0

for i in range(len(schematic)):
    for j in range(len(schematic[i])):
        if schematic[i][j] == "*":
            gears += 1
            numbers = []
            print(i,j)
            # To the left
            if schematic[i][j-1].isnumeric():
                if schematic[i][j-2].isnumeric():
                    if schematic[i][j-3].isnumeric():

                        numbers.append(int(schematic[i][j-3]) * 100 + int(schematic[i][j-2]) * 10 + int(schematic[i][j-1]))
                    else:
                        numbers.append(int(schematic[i][j-2]) * 10 + int(schematic[i][j-1]))
                else:
                    numbers.append(int(schematic[i][j-1]))

            # To the right
            if schematic[i][j+1].isnumeric():
                if schematic[i][j+2].isnumeric():
                    if schematic[i][j+3].isnumeric():

                        numbers.append(int(schematic[i][j+1]) * 100 + int(schematic[i][j+2]) * 10 + int(schematic[i][j+3]))
                    else:
                        numbers.append(int(schematic[i][j+1]) * 10 + int(schematic[i][j+2]))
                else:
                    numbers.append(int(schematic[i][j+1]))

            # Strictly on top
            if schematic[i-1][j].isnumeric(): #--0--
                # Checking to the left
                if schematic[i-1][j-1].isnumeric(): #-00--
                    # Check for X000X
                    if schematic[i-1][j+1].isnumeric(): # X000X
                        numbers.append(int(schematic[i-1][j-1]) * 100 + int(schematic[i-1][j]) * 10 + int(schematic[i-1][j+1]))
                    else: # -00XX
                        if schematic[i-1][j-2].isnumeric(): # 000XX
                            numbers.append(int(schematic[i-1][j-2]) * 100 + int(schematic[i-1][j-1]) * 10 + int(schematic[i-1][j]))
                        else: # X00XX
                            numbers.append(int(schematic[i-1][j-1]) * 10 + int(schematic[i-1][j]))
                else: # XX0--
                    if schematic[i-1][j+1].isnumeric():  # XX00-
                        if schematic[i-1][j+2].isnumeric(): # XX000
                            numbers.append(int(schematic[i-1][j]) * 100 + int(schematic[i-1][j+1]) * 10 + int(schematic[i-1][j+2]))
                        else: # XX00X
                            numbers.append(int(schematic[i - 1][j]) * 10 + int(schematic[i - 1][j+1]))
                    else: # XX0XX
                        numbers.append(int(schematic[i-1][j]))
            else:
                # Diag up left
                if schematic[i-1][j - 1].isnumeric():
                    if schematic[i-1][j - 2].isnumeric():
                        if schematic[i-1][j - 3].isnumeric():

                            numbers.append(int(schematic[i-1][j - 3]) * 100 + int(schematic[i-1][j - 2]) * 10 + int(
                                schematic[i-1][j - 1]))
                        else:
                            numbers.append(int(schematic[i-1][j - 2]) * 10 + int(schematic[i-1][j - 1]))
                    else:
                        numbers.append(int(schematic[i-1][j - 1]))

                # Diag up right
                if schematic[i-1][j + 1].isnumeric():
                    if schematic[i-1][j + 2].isnumeric():
                        if schematic[i-1][j + 3].isnumeric():

                            numbers.append(int(schematic[i-1][j + 1]) * 100 + int(schematic[i-1][j + 2]) * 10 + int(
                                schematic[i-1][j + 3]))
                        else:
                            numbers.append(int(schematic[i-1][j + 1]) * 10 + int(schematic[i-1][j + 2]))
                    else:
                        numbers.append(int(schematic[i-1][j + 1]))

            # Strictly down
            if schematic[i+1][j].isnumeric(): #--0--
                # Checking to the left
                if schematic[i+1][j-1].isnumeric(): #-00--
                    # Check for X000X
                    if schematic[i+1][j+1].isnumeric(): # X000X
                        numbers.append(int(schematic[i+1][j-1]) * 100 + int(schematic[i+1][j]) * 10 + int(schematic[i+1][j+1]))
                    else: # -00XX
                        if schematic[i+1][j-2].isnumeric(): # 000XX
                            numbers.append(int(schematic[i+1][j-2]) * 100 + int(schematic[i+1][j-1]) * 10 + int(schematic[i+1][j]))
                        else: # X00XX
                            numbers.append(int(schematic[i+1][j-1]) * 10 + int(schematic[i+1][j]))
                else: # XX0--
                    if schematic[i+1][j+1].isnumeric():  # XX00-
                        if schematic[i+1][j+2].isnumeric(): # XX000
                            numbers.append(int(schematic[i+1][j]) * 100 + int(schematic[i+1][j+1]) * 10 + int(schematic[i+1][j+2]))
                        else: # XX00X
                            numbers.append(int(schematic[i + 1][j]) * 10 + int(schematic[i + 1][j+1]))
                    else: # XX0XX
                        numbers.append(int(schematic[i+1][j]))
            else:
                # Diag up left
                if schematic[i+1][j - 1].isnumeric():
                    if schematic[i+1][j - 2].isnumeric():
                        if schematic[i+1][j - 3].isnumeric():

                            numbers.append(int(schematic[i+1][j - 3]) * 100 + int(schematic[i+1][j - 2]) * 10 + int(
                                schematic[i+1][j - 1]))
                        else:
                            numbers.append(int(schematic[i+1][j - 2]) * 10 + int(schematic[i+1][j - 1]))
                    else:
                        numbers.append(int(schematic[i+1][j - 1]))

                # Diag up right
                if schematic[i+1][j + 1].isnumeric():
                    if schematic[i+1][j + 2].isnumeric():
                        if schematic[i+1][j + 3].isnumeric():

                            numbers.append(int(schematic[i+1][j + 1]) * 100 + int(schematic[i+1][j + 2]) * 10 + int(
                                schematic[i+1][j + 3]))
                        else:
                            numbers.append(int(schematic[i+1][j + 1]) * 10 + int(schematic[i+1][j + 2]))
                    else:
                        numbers.append(int(schematic[i+1][j + 1]))
            print(numbers)
            if len(numbers) == 2:
                legalgears += 1
                total += numbers[0]*numbers[1]
                print(total)

print(gears)
print(legalgears)

print(total)