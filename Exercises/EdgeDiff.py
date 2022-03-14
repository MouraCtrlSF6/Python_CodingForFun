def edge_diff(One, Two):
    return 2(One**2 - Two**2)

rOne = int(input("Type a radius: "))
rTwo = int(input("Type another radius: "))
print("Difference between the two areas: ", edge_diff(rOne, rTwo))