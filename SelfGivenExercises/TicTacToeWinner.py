def ttt (table):
    if table[0][0]==table[1][1] and table[1][1]==table[2][2]:
        return table[0][0]
    if table[0][2]==table[1][1] and table[2][0]==table[1][1]:
        return table[0][2]
    for i in range(len(table)):
        if table[i][0]==table[i][1] and table[i][1]==table[i][2]:
            return table[i][0]
        if table[0][i]==table[1][i] and table[1][i]==table[2][i]:
            return table[0][i]  
    return "draw!"

table=(
  ["X", "O", "X"],
  ["X", "O", "O"],
  ["O", "O", "X"]
)
winner = ttt(table)
print(winner)