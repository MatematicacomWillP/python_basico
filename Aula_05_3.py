#== MANIPULAÇÃO DE LISTAS ==#
#(UFF)
#3) Faça um programa que percorre uma lista com o seguinte formato: 
#   [['Brasil', 'Italia', [9, 9]], ['Brasil', 'Espanha', [5, 8]], 
#   ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez 
#   em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas 
#   e a Itália fez 9. O programa deve imprimir na tela:  
#   (a) o total de faltas do campeonato 
#   (b) o time que fez mais faltas 
#   (c) o time que fez menos faltas 

jogos = [['Brasil', 'Italia', [9, 9]], ['Brasil', 'Espanha', [5, 8]], ['Italia', 'Espanha', [7,8]]]

times = []
n_faltas = []

#TOTAL DE FALTAS NO CAMPEONATO
total_faltas = 0
for jogo in jogos:
    for i in range(2):
        total_faltas += jogo[2][i]

#SEPARANDO OS VALORES PARA CADA LISTA TIMES E FALTAS
        if jogo[i] not in times:
            n_faltas.append(jogo[2][i])
            times.append(jogo[i])
        else:
            index = times.index(jogo[i])
            n_faltas[index] = jogo[2][i]

#COMPARAÇÃO ENTRE MAIOR E MENOR FALTAS
mais = times[0]
menos = times[0]
for (t,f) in zip(times[1:],n_faltas[1:]):
    if f > n_faltas[times.index(mais)]:
        mais = t
    elif f < n_faltas[times.index(menos)]:
        menos = t


print('O campeonato teve o total de %d faltas.' %total_faltas)
print('O time que fez mais faltas foi o: %s' %mais)
print('O time que fez menos faltas foi o: %s' %menos)