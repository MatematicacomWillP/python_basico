#== REPETIÇÃO LOOP WHILE ==#

#1) Fazer um progrma que calcule o fatorial de um 
#   número seguindo o exemplo:
#   5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input("Entre com um número: "))
f = 1
print('{}! = '.format(n),end='')
while n > 0:
    print('{}'.format(n),end='')
    print(' x ' if n > 1 else ' = ',end='')
    f *= n
    n -= 1  
print(f)