def info(x):
    a = x/6 #total litros
    b = a/18    #total latas 18litros float
    c = a/3.6   #total latas 3.6litros float
    qntd_ideal = 18*(int(b) + 1) + 3.6*(int(c) + 1)   #diferença máxima entre o comprado e o necessitado
    b_ideal = b
    c_ideal = c
    #com latas de 18 litros
    if b > int(b):
        b = int(b)+1
    else:
        b = int(b)
    b_value = 80*b  
    #com latas de 3.6 litros
    if c > int(c):
        c = int(c)+1
    else:
        c = int(c)
    c_value = 25*c  
    #misturando as latas
    if b_value > c_value:
        preco_ideal = c_value
    else:
        preco_ideal = b_value
    #varia i até a quantidade de SÓ galões de 18 litros    
    for i in range(b+1):
        #varia j até a quantidade de SÓ galões de 3.6 litros
        for j in range(c+1):
            #verifica quantidade de tinta cada uma das possibilidades de compra
            n = i*18 + j*3.6
            #verifica o preço de cada uma das possibilidades
            preco = 80*i + 25*j
            #se a quantidade de tinta for maior ou igual a necessitada
            if n >= a:
                #se as sobras forem menores que a menor sobra registrada e o preço for menor que o menor preço registrado, salva essas possibilidade da memória
                if n - a <= qntd_ideal and preco <= preco_ideal:
                    qntd_ideal = n - a
                    preco_ideal = preco
                    b_ideal = i
                    c_ideal = j
    return b, b_value, c, c_value, b_ideal, c_ideal, preco_ideal 

print("\n--------------------------------------------------------------------------------------------")   
print("\nO programa objetiva informar ao consumidor a forma mais barata de se comprar galões de tinta,\nfornecendo-se a área que deve ser pintada, em metros quadrados. São dados:")
print("-- Galão de 18 litros: R$80,00")
print("-- Galão de 3.6 litros: R$25,00\n")
x = float(input("Informe quantos metros quadrados devem ser pintados: "))
y = info(x)
print("\nApenas com galões de 18 litros: ")
print(y[0],"galões, totalizando R$",y[1])
print("\nApenas com galões de 3.6 litros: ")
print(y[2],"galões, totalizando R$",y[3])
print("\nMisturando-se galões de 18 litros com galões de 3.6 litros: ")
print(y[4],"galões de 18 litros e",y[5],"galões de 3.6 litros.\nTotal = R$",y[6],"\n\n")