# Declaração de variáveis
vet = []*10
par = []*1
impar = []*1
print("\nO programa separa valores paras e impares.\n10 valores devem ser inseridos.\n")
# Entrada de valores
for i in range(10):
    vet.append(int(input(f"Digite o {i+1}º valor: ")))
# Separacao dos pares
for i in range(len(vet)):
    if vet[i]%2 == 0:
        par.append(vet[i])
# Separacao dos impares
for i in range(len(vet)):
    if vet[i]%2 != 0:
        impar.append(vet[i])
# Exibicao dos resultados
print("\nValores pares: ", par)
print("Valores impares: ", impar)
print("Todos os valores: ", vet)
print("\n")