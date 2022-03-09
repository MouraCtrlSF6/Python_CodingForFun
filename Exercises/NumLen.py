import math
def math_numlen(x):
    a = int(math.log10(x))
    return a + 1
    
def num_len(x):
    i = 0
    while x >= 1:
        x = x/10
        i += 1
    return i

x = int(input("Type a number: "))
#Choose what function you're gonna use
#x = math_numlen(x)
#x = num_len(x)
print("Number length: ", x)