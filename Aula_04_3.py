#== REPETIÇÃO LOOP FOR ==#

#3) Fazer um programa que imprima a tabuada de um número de 
#   1 a 10.

n = int(input('Entre com um número: '))
for i in range(1,11):
    print('{} x {} = {}'.format(n,i,n*i))