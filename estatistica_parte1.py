#== ESTATÍSITCA SIMPLES ==#
#(UFRJ)
#1) Os resultados baseados em uma escala de ansiedade para uma 
#   amostra de nove sujeitos são:  
#       67 75 63 72 77 78 81 77 80 
#   Determinar: [moda, média e mediana]

#== Entrada de dados ==#

dados = []
valores = input('Digite os valores: ')
dados.append(valores)
while True:
    if valores == 'pare':
        break
    else:
        valores = input('Digite os valores: ')
        dados.append(valores)
dados.pop() #== Retira o último valor da lista ==#
dados1 = [float(i) for i in dados] #== Transforma string em float ==#
dados1.sort() #== Coloca valores em ordem crescente ==#
print('O roll de dados:\n{}'.format(dados1))

#== FAZENDO A MÉDIA ARITMÉTICA ==#

soma = 0
for i in dados1:
    soma += i
media = soma/len(dados1)
print('A média = {}'.format(round(media,2)))

#== FAZENDO O CÁLCULO DA MEDIANA ==#

n = len(dados1)
if n % 2 == 0:
    metade1 = dados1[n // 2]
    matade2 = dados1[(n // 2) - 1]
    mediana = (metade1 + matade2) / 2    
else:
    mediana = dados1[n // 2]
print('A madiana é: {}'.format(mediana))