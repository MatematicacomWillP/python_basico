#== REPETIÇÃO LOOP WHILE ==#

#2) Escreva um programa que receba várias idades e que calcule 
#   e mostre a média das idades digitadas. Finalize digitando 
#   a idade igual a zero

idade = soma = cont = 0
idade = int(input('Digite uma idade: '))
while idade != 0:
    soma += idade
    cont += 1
    idade = int(input('Digite uma idade: '))
media = soma/cont
print("A soma das idades = {} e a média = {}".format(soma,media))