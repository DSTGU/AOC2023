cards = open("input.txt").readlines()

total = 0

def check_card(id):
    global total
    total+=1
    seg = cards[id].split(":")
    nums = seg[1].split("|")
    winarray = nums[0].split()
    yourarray = nums[1].split()

    win = 0

    for x in yourarray:
        if x in winarray:
            win+=1

    for i in range(id+1,id+1+win):
        check_card(i)



for card in range(len(cards)):
    print(card,total)
    total +=1
    seg = cards[card].split(":")
    nums = seg[1].split("|")
    winarray = nums[0].split()
    yourarray = nums[1].split()
    win = 0

    for x in yourarray:
        if x in winarray:
            win+=1

    for i in range(card+1,card+1+win):
        check_card(i)

print(total)
