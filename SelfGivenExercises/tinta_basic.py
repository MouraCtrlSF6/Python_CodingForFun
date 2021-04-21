def info(x):
    a = x/3
    a = a/18
    if a > int(a):
        a = int(a)+1
    else:
        a = int(a)
    value = 80*a
    return a, value
    
x = float(input("Informe quantos metros quadrados devem ser pintados: "))
y = info(x)
print("Devem ser usados", y[0],"galões de tinta, com um total de R$",y[1],)