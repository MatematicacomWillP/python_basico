#== MANIPULAÇÃO DE LISTAS ==#
#(UNICAMP)
#2) Dadas duas listas P1 e P2, ambas com n valores reais que representam as notas
#   de uma turma na prova 1 e na prova 2, respectivamente, escreva um programa que 
#   calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma obteve a 
#   melhor média. 
#   Exemplo: 
#   Tamanho da turma: 5 
#   P1: 7.0 8.3 10.0 6.5 9.3 
#   P2: 8.5 6.9 5.0 7.5 9.8 
#   Resposta: 
#   Média da turma na prova 1: 8.22 
#   Média da turma na prova 2: 7.54 
#   A turma obteve a melhor média na prova 1.

qprovas = int(input('Digite a quantidade de provas: '))
qalunos = int(input('Digite a quantidade de alunos da turma: '))

provas_turma = []
for provas in range(qprovas):
    notas_alunos = []
    for notas in range(qalunos):
        notas_alunos.append(float(input('Prova ' + str(provas+1) + ' aluno ' + str(notas+1) + ': ')))
    provas_turma.append(notas_alunos)
print(provas_turma)

#SOMATÓRIO DAS NOTAS
notas_soma = [sum(x) for x in provas_turma]
print(notas_soma)

#MÉDIA DAS NOTAS
media_notas = []
p = []
for j in range(qprovas):
    p.append(j+1)
    for i in notas_soma:
        m = i/qalunos
        media_notas.append(m)
    print('Média da turma na prova ' + str(j+1) + ': ',round(media_notas[j],2))

#MAIOR VALOR
mais = p[0]
for (p1,m1) in zip(p[1:],media_notas[1:]):
    if m1 > media_notas[p.index(mais)]:
        mais = p1
print('A turma obteve a melhor média na prova %s' %mais)