#== ESTATÍSTICA INTERVALO DE CLASSE ==#

import math
from pandas import*

#== Entrada de dados ==#

dados = []
entrada = input('Digite os valores: ')
dados.append(entrada)
while True:
    if entrada == 'pare':
        break
    else:
        entrada = input('Digite os valores: ')
        dados.append(entrada) 
dados.pop()
dados = [float(i) for i in dados]
dados.sort()
print(dados)

#== Número de Classes ==#
n = len(dados)
k = 1 + 3.3*(math.log10(n)) #= Regra de Sturges =#

decimal = k - int(k)
if decimal <= 0.5:
    k = int(k)
    print('O número de Classes: {}'.format(k))
else:
    k = math.ceil(k)
    print('O número de Classes: {}'.format(k))

#== Amplitude do Intervalo ==#

max1 = max(dados)
min1 = min(dados)
At = max1 - min1
h = At/k
h = math.ceil(h)
print('A amplitude do intervalo: ',h)

#== Montando o Intervalo ==#

classe = []
bins = []
menor = min1
max_amp = menor + h
valor = menor
bins.append(valor)
while valor < max1:
    classe.append('{}|--{}'.format(valor,valor + h))
    valor += h
    bins.append(valor)

#== Contando as Frequências ==#
for i in dados:
    ultimo = i
if ultimo == max1:
    fr = cut(dados, bins=k, labels=classe, right=False, include_lowest=False).value_counts()
else:
    fr = cut(dados, bins, labels=classe, right=False, include_lowest=False).value_counts()
print(fr)