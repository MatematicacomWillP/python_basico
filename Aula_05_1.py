#== MANIPULAÇÃO DE LISTAS ==#
#(UFF)
#1) Faça um programa que percorre duas listas e
#   intercala os elementos de ambas, formando uma
#   uma terceira lista. A terceira lista deve começar 
#   pelo primeiro elemento da lista menor.

#   Exemplo:
#   lista1 = [1,2,3,4]
#   lista2 = [10,20,30,40,50,60]
#   lista_intercalada = [1,10,2,20,3,30,4,40,50,60]

lista1 = [1,2,3,4]
lista2 = [10,20,30,40,50,60]
lista_intercalada = [x for i in zip(lista1,lista2) for x in i]
y = lista2[len(lista1):]
print(lista_intercalada + y)