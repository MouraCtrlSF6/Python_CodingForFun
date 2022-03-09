import sys
n = 0
def sum(a, i):
    if (i != n):
        a = (1/(i+1)) + sum(a, i+1)
    return a
print("Soma dos termos da sequencia: 1, 1/2, 1/3, 1/4... 1/n")
n = int(input('Quantos termos você quer somar? '))
try:
    print(f'Resultado: {round(sum(0, 0), 2)}\n\n')
except RecursionError:
    print("Máximo de termos excedido. Por favor, some menos de 998 termos.\n\n")