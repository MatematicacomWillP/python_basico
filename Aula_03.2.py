#== EXERCÍCIO CONDICIONAIS ==#

#2) Escreva um programa que, dado o valor de venda, imprima a
#   a comissão que deverá ser paga ao vendedor. Para calcular
#   a comissão, considere a tabela abaixo:
#   ___________________________________________________________ 
#            Venda mensal            |       Comissão
#   >= R$ 100.000,00                 |R$700,00 + 16% das vendas
#   < R$100.000,00 e >= R$80.000,00  |R$650,00 + 14% das vendas
#   < R$80.000,00  e >= R$60.000,00  |R$600,00 + 14% das vendas
#   < R$60.000,00  e >= R$40.000,00  |R$550,00 + 14% das vendas
#   < R$40.000,00  e >= R$20.000,00  |R$500,00 + 14% das vendas
#   < R$20.000,00                    |R$400,00 + 14% das vendas

# >= (maior ou igual); < (menor que)

vendas = float(input("Digite o valor de venda do mês: "))

if vendas >= 100000:
    comissao = 700 + (0.16*vendas)
    print('O valor da comissão a ser pago é de R$ {:.2f}'.format(comissao))
elif vendas < 100000 and vendas >= 80000:
    comissao = 650 + (0.14*vendas)
    print('O valor da comissão a ser pago é de R$ {:.2f}'.format(comissao))
elif vendas < 80000 and vendas >= 60000:
    comissao = 600 + (0.14*vendas)
    print('O valor da comissão a ser pago é de R$ {:.2f}'.format(comissao))
elif vendas < 60000 and vendas >= 40000:
    comissao = 550 + (0.14*vendas)
    print('O valor da comissão a ser pago é de R$ {:.2f}'.format(comissao))
elif vendas < 40000 and vendas >= 20000:
    comissao = 500 + (0.14*vendas)
    print('O valor da comissão a ser pago é de R$ {:.2f}'.format(comissao))
else:
    comissao = 400 + (0.14*vendas)
    print('O valor da comissão a ser pago é de R$ {:.2f}'.format(comissao))