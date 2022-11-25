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
c = [] #Média do intervalo de classe
menor = min1
max_amp = menor + h
valor = menor
bins.append(valor)
while valor < max1:
    classe.append('{} |-- {}'.format(valor,valor + h))
    media = (valor + (valor+h))/2
    valor += h
    bins.append(valor)
    c.append(media)

#== Contando as Frequências ==#

for i in dados:
    ultimo = i

if ultimo == max1:
    fi = cut(dados, bins=k, right=False, include_lowest=False).value_counts().to_list()
else:
    fi = cut(dados, bins, right=False, include_lowest=False).value_counts().to_list()
print(fi)

Fi = [] #Frequência absoluta acumulada
fr = [] #Frequência relativa
Fri = [] #Frequência relativa acumulada

soma1 = 0 #Fi
soma2 = 0 #Fri
for i in fi:
    soma1 += i
    Fi.append(soma1)
    div = i/n
    fr.append('{:.3f}'.format(div))
    soma2 += div
    Fri.append('{:.3f}'.format(soma2))
    
df = DataFrame({'Classe':classe, 'fi':fi, 'Fi':Fi, 'fr':fr, 'Fr':Fri, 'c':c})
df = df.to_string(index = False)
print(df)