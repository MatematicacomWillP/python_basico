#== EXERCÍCIO CONDICIONAIS ==#

#1) Os ovos custam R$ 1,00 cada se forem compradas menos
#   do que uma dúzia, e R$ 0,50 se forem compradas pelo menos doze.
#   Escreva um programa que leia o número de ovos comprados, calcule 
#   e escreva o valor total da compra.

ovos = int(input("Digite a quantidade de ovos: "))

if ovos < 12:
    total = 1 * ovos 
    print('O valor da minha compra é de R$ {},00' .format(total))
else:
    total = 0.50 * ovos
    print('O valor da minha compra é de R$ {:.2}' .format(total))