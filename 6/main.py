import math

lines = open("input.txt").readlines()
time = lines[0].replace(" ", "").strip().split(":")
distance = lines[1].replace(" ", "").split(":")
#Remove the .replace and .split parts for 1st task

print(time)
print(distance)

def review(t, d):
    # -x^2 + tx - d = 0

    dis = math.sqrt(t*t - 4*d)
    x1 = (-t-dis)/(-2)
    x2 = (-t+dis)/(-2)
    #print(x1,x2)

    if x1 > x2 :
        t = x2
        x2 = x1
        x1 = t

    x1r = math.floor(x1) + 1
    x2r = math.ceil(x2)
    #print(list(range(x1r,x2r)))
    return len(list(range(x1r,x2r)))

total = 1
for i in range(1,len(time)):
    total *= review(int(time[i]), int(distance[i]))

print(total)