def josephus(n):
    i=0
    while 2**i <= n:
        i+=1
    n = 2*n+1 - 2**i
    return n

n = int(input("Type how many people there is on the circle: "))
n = josephus(n)
print(f"Stay in the {n}th position, it's safe there!\n\n")