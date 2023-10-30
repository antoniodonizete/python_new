'''
Listas em Python
Tipo list - Mutável
# 
'''
#        01234
#       -54321
string = 'ABCDE' # 5 caracteres
i = 0
# lista = list() 
lista = [123, True, 'Antonio',1.2, [] ]

print(lista[0], 'indice 0 da lista')
print(lista[2], 'indice 2 da lista')
print(lista[1], 'indice 1 da lista')
for i in lista:
    print([i])
#    [i] += 1
print(lista[2], 'indice 2 da lista')
lista[2] = 'Antonio Donizete' # alterando item 2 lista 
print(lista[2], 'indice 2 da lista alterado')
print(lista[2].upper(), 'agora maiusculo')
lista.__format__()
print(lista.count)