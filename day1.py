import re

sum = 0
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def tonum(n):
    if n in digits:
        return int(n)
    if n in nums:
        return nums.index(n)+1

f = open("input.txt", "r")
lines = f.read().split("\n")
for l in lines:
    """
    v1 = 0
    v2 = 0
    i1 = len(l)
    i2 = 0
    for n in digits:
        i1n = l.find(n)
        if i1n < i1:
            i1 = i1n
            v1 = int(n)
        i2n = l.rfind(n)
        if i2n > i2:
            i2 = i2n
            v2 = int(n)
    for n in digits:
        i1n = l.find(n)
        if i1n < i1:
            i1 = i1n
            v1 = nums.index(n) + 1
        i2n = l.rfind(n)
        if i2n > i2:
            i2 = i2n
            v2 = nums.index(n) + 1
    """

    
    list = re.findall("[0-9]|one|two|three|four|five|six|seven|eight|nine", l)
    val = tonum(list[0])*10 + tonum(list[len(list)-1])
    print(val)
    sum += val

error = 4
print(sum-error)