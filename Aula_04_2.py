#== REPETIÇÃO LOOP FOR ==#

#2) Fazer um progrma que calcule o fatorial de um 
#   número seguindo o exemplo:
#   5! = 5 x 4 x 3 x 2 x 1 = 120

#float = número com vírgula
#int = número inteiro

n = int(input("Entre com um número: "))
f = 1
print('{}! = '.format(n),end='')
for i in range(n,0,-1):
    print('{}'.format(i),end='')
    print(' x ' if i>1 else' = ',end='')
    f*=i
print(f)
