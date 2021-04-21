def edge_diff(r):
    diff = 2*r**2
    return diff

r = int(input("Type a radius: "))
r = edge_diff(r)
print("Difference between the two areas: ", r)