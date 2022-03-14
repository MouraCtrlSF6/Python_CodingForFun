print("\nO programa separa valores paras e impares.\n10 valores devem ser inseridos.\n")

# Declaração de variáveis
vet = []
par = []
impar = []

# Entrada de valores
for i in range(10):
    vet.append(int(input(f"Digite o {i+1}º valor: ")))

# Separacao dos pares e ímpares
for value in vet:
    if value % 2 == 0:
        par.append(value)
    else:
        impar.append(value)
        
# Exibicao dos resultados
print("\nValores pares: ", par)
print("Valores impares: ", impar)
print("Todos os valores: ", vet)
print("\n")