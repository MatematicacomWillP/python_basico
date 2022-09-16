#==> Exemplo 1 --> Condicionais 
#   Faça um programa que receba dois números e 
#   mostre qual deles é o maior, e se caso for iguais, 
#   mostrar a mensagem dizendo que são iguais.

valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))

if valor1 > valor2:
    print('Valor 1: {} é maior que o Valor 2: {}'.format(valor1,valor2))
elif valor2 > valor1:
    print('Valor 2: {} é maior que o Valor 1: {}'.format(valor2,valor1))
else:
    print('Valor 1: {} é igual ao Valor 2: {}'.format(valor1,valor2))