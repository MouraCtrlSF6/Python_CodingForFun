n = {}
while 1:
    for x in range(4):
        n[x] = float(input(f"Type the {x+1}º score: "))
        while(n[x] > 10.0 or n[x] < 0.0):
            n[x] = float(input("Value not valid. Please, type a valid score: "))
    print(f"\nThe media was {round((n[0]+n[1]+n[2]+n[3])/4, 2)}\n\n")
    y = input("Wanna continue? ")
    while y!="yes" and y!="no":
        y = input("Invalid value. Please, type yes ou no: ")
    if y=="no":
        break