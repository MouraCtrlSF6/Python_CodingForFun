def josephus(n):
  i=0
  while 2**i <= n:
    i+=1

  return 2*n+1 - 2**i

n = int(input("Type how many people there is on the circle: "))
print(f"Stay in the {josephus(n)}th position, it's safe there!\n\n")