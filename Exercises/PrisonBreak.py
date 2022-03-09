cell = list(input("Type a cell combination: "))
index = 0
freed = 0
i = 0
for count in range(len(cell)):
    if not int(cell[count]) == 1 and not int(cell[count]) == 0:
        print("Only binary arguments are accepted!")
        exit()
if not int(cell[0]) == 0:
    while index+i<len(cell):
        if int(cell[index+i]) == 1:
            index+=i
            freed+=1
            i=-1
            for j in range(len(cell)):
                if cell[j] == '1': 
                    cell[j] = '0'
                else: cell[j] = '1'
        i+=1
print(f"You freed {freed} prisioners!")