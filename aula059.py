# Desempacotampento em camadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #  0       1
    ['Maria', 'Helena'], #0
    #  0
    ['Elaine'],  #1
    #  0        1        2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20,30, 40)], #2
]

# a, b, c = lista
# print(a, c)

# lista = primeiro, ultimo e ante penultimo
# p, b, *_, ap, u = lista
# print(p, u, ap)

print(*salas, sep='\n') #faz um for na lista, item linha a linha