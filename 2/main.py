games = open("input.txt").readlines()

powersum = 0

for game in games:
    print(game)
    a = game.split(":")
    rolls = a[1].split(";")
    id = int(a[0].split(" ")[1])
    print(id)
    legalflag = 1
    redmin = 0
    greenmin = 0
    bluemin = 0
    for roll in rolls:
        colors = roll.split(",")
        for color in colors:
            splits = color.split(" ")
            match splits[2].strip():
                case "red":
                    if int(splits[1]) > redmin:
                        redmin = int(splits[1])
                case "green":
                    if int(splits[1]) > greenmin:
                        greenmin = int(splits[1])
                case "blue":
                    if int(splits[1]) > bluemin:
                        bluemin = int(splits[1])


    print(redmin, greenmin, bluemin, (redmin * greenmin * bluemin))
    powersum += (redmin * greenmin * bluemin)

print(powersum)