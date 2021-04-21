#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
#cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
#e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da 
#compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
def compra(meat, kg, card):
    cartao = 0
    sim = ['sim', 'SIM', 'Sim']
    nao = ['nao', 'NAO', 'não', 'NÃO', 'Nao', 'Não']
    if kg>5:
        price = (meat+4.8)*kg
    else:
        price = (meat+3.9)*kg
    
    for i in sim:
        if card == i: cartao = 1
    for i in nao:
        if card == i: cartao = 2
    while cartao == 0:
        card = input('Resposta nao valida. Por favor, digite "sim" ou "nao": ')
        for i in sim:
            if card == i: cartao = 1
        for i in nao:
            if card == i: cartao = 2       

   
    if cartao == 1:
        price = price*0.95

    return price
      

print('\n\nBom tarde!')
print('                          Até 5 Kg           Acima de 5 Kg')
print('1 - File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg')
print('2 - Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
print('3 - Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')
meat = int(input('\nQual o tipo de carne? '))
kg = float(input('Quantos kilos de carne você deseja? '))
card = input('Deseja usar o cartão Tabajara? ')

preco = compra(meat, kg, card)
print(f"Valor total da compra: R${round(preco, 2)}")
print('Volte Sempre!\n\n')