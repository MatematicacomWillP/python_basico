#== ESTATÍSTICA INTERVALO DE CLASSE ==#

import math
from pandas import*
from matplotlib import pyplot as plt

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
Xi = [] #Média do intervalo de classe
menor = min1
max_amp = menor + h
valor = menor
bins.append(valor)
while valor < max1:
    classe.append('{} |-- {}'.format(valor,valor + h))
    ponto_medio = (valor + (valor+h))/2
    valor += h
    bins.append(valor)
    Xi.append(ponto_medio)

#== Contando as Frequências ==#

for i in dados:
    ultimo = i

if ultimo == max1:
    fi = cut(dados, bins=k, right=False, include_lowest=False).value_counts().to_list()
    plt.style.use('fivethirtyeight')
    plt.hist(dados, bins=k, edgecolor='black')
else:
    fi = cut(dados, bins, right=False, include_lowest=False).value_counts().to_list()
    plt.style.use('fivethirtyeight')
    plt.hist(dados, bins=bins, edgecolor='black')
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

#= Medidas de Dispersão =#

Xf = list(zip(Xi,fi))
XiFi = []
soma3 = 0
for i, j in Xf: # for i, j in zip(Xi,fi): #
    i *= j
    XiFi.append(i)
    soma3 += i
mediaX = soma3/n
print('A média de Xi x Fi = ', mediaX)


#= (Xi - mediaX); (Xi - mediaX)^2 =#
XimediaX = []
XimediaX2 = []
for i in Xi:
    sub = i - mediaX
    XimediaX.append(sub)
    XimediaX2.append(sub**2)

Xi2f = list(zip(XimediaX2,fi))
XimediaX2fi = []
soma4 = 0
for i, j in Xi2f:
    i *= j
    XimediaX2fi.append(i)
    soma4 += i

Variancia = soma4/n
Desvio_Padrao = math.sqrt(Variancia)
C_V = (Desvio_Padrao/mediaX)*100



df = DataFrame({'Classe':classe, 'fi':fi, 'Xi':Xi, 'Xi*fi':XiFi, 'Xi-mediaX':XimediaX, '(Xi-mediaX)^2':XimediaX2, '(Xi-mediaX)^2*fi':XimediaX2fi })
df = df.to_string(index = False)
print(df)

print('A variância = ', Variancia)
print('O Desvio Padrão =', Desvio_Padrao)
print('O Coeficiente de Variação = {:.2f}%'.format(C_V))

plt.xticks(bins)
plt.plot(Xi,fi, 'o-',color='red')
for x, y in zip(Xi,fi):
    label = f'{x}'
    plt.annotate(label, (x,y), textcoords='offset points', xytext=(0,10), ha='center')
plt.show()