def next_edge(a,b):
    c = a + b - 1
    return c
    
a = int(input("Type an edge of a triangle: "))
b = int(input("Type the next of the same triangle: "))
c = next_edge(a,b)
print("Maximum integer edge: ", c)	