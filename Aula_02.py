#== CONDICIONAIS ==#

# if --> se
# else --> senão

#== SINAIS ==#

# > maior   == igual       >= maior ou igual
# < menor   != diferente   <= menor ou igual

#==> Exemplo 1 --> Condicionais
#   A nota final de um estudante é calculada a partir de 
#   três notas atribuídas entre o intervalo de 0 até 10, 
#   respectivamente, nota 1, nota 2
#   e a nota 3. A média das três notas mencionadas 
#   anteriormente obedece aos pesos: Nota 1: 2; 
#   Nota 2: 3; Nota 3: 5. De acordo com o resultado, 
#   mostre na tela se o aluno está reprovado (média entre 0 e 2,9), 
#   de recuperação (entre 3 e 4,9) ou se foi aprovado.

n1 = float(input("Digite o valor da nota 1: "))
n2 = float(input("Digite o valor da nota 2: "))
n3 = float(input("Digite o valor da nota 3: "))

media = ((n1*2)+(n2*3)+(n3*5))/10
if media >= 0 and media <= 2.9:
    print('A média deste aluno foi de {} e está reprovado'.format(media))
elif media >= 3 and media <= 4.9:
    print('A média deste aluno foi de {} e está em recuperação'.format(media))
else:
    print('A média deste aluno foi de {} e está aprovado'.format(media))
