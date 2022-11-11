#== ESTATÍSTICA ==#
#(VUNESP - TJM/SP - 2017)
#2) A tabela apresenta o número de acertos dos 600 candidatos 
#   que realizaram a prova da segunda fase de um concurso, que continha 
#   5 questões de múltipla escolha.
#   ____________________________________________________
#   xi => NÚMERO DE ACERTOS | NÚMERO DE CANDIDATOS => fi
#           5               |         204
#           4               |         132
#           3               |          96
#           2               |          78
#           1               |          66
#           0               |          24
#   ----------------------------------------------------
#   A média de acertos por prova foi de:                    

#== média_ponderada = (soma Xi * fi) / (soma fi)

#== Entrando com os valores ==#
xi = []
fi = []
x = input("Entre com os valores de xi: ")
f = input("Entre com os valores de fi: ")
xi.append(x)
fi.append(f)
while True:
    if x == 'pare' and f == 'pare':
        break
    else:
        x = input("Entre com os valores de xi: ")
        f = input("Entre com os valores de fi: ")
        xi.append(x)
        fi.append(f)
xi.pop()
fi.pop()
xi1 = [float(i) for i in xi]
fi1 = [float(i) for i in fi]

#== Fazendo o cálculo da média ponderada ==#
L1 = list(zip(xi1,fi1))

soma1 = 0
soma2 = 0
for x1, f1 in L1:
    numerador = x1 * f1
    soma1 += numerador
    soma2 += f1
media_pond = soma1/soma2
print('O valor da média ponderada é {:.2f}'.format(media_pond))