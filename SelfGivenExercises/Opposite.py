print("Enter some data and it'll be printed in the opposite order.\nMax number of characters: 10.\nEnter a Null character to finish\n\n")
vet = []*1
for i in range(10):
    vet.append(input(f"Type the {i+1} data: "))
    if(vet[i] == ''):
        break
print("\nData in the typed order: ")
for directOrder in vet:
    if(directOrder != ''):
        print(directOrder)
print("\nData in the opposite order: ")
for oppositeOrder in range(len(vet)-1, -1, -1):
    if (vet[oppositeOrder] != ''):
        print(vet[oppositeOrder])
