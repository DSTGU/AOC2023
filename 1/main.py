asd = open("input.txt").readlines()

total = 0

dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

print(dic)

for i in asd:
    first = "x"
    last = "x"
    print(i)
    for char in range(len(i)):
        if i[char].isnumeric():
            if first == "x":
                first = i[char]
            last = i[char]
        else:
            for intt in range(10):

                if dic[intt] == i[ char : char+len(dic[intt])]:
                    if first == "x":
                        first = str(intt)
                    last = str(intt)


    con = int(first+last)
    print(con)
    total += con



print(total)
