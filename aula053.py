
# lista = ['Maria', 'Luiz', 'Helena']
# lista.append('joão')

# indices = range(len(lista))

# for indice in indices:

#     print(indice,lista[indice], type(lista[indice]))
# print("*" * 50)

# lista = ['Maria', 'Luiz', 'Helena']
# lista.append('joão')

# for item in enumerate(lista):
#     indice, nome = item
#     print('Enumerate:')
#     print(indice, nome)

# print("*" * 50)

# for item in enumerate(lista):
#     for valor in item:
#         print(valor)
    
# print("* " * 50)

lista = 'tomate', 'cebola', 'vinagre', 'alho', 'pimenta'

for indice, item in enumerate(lista, start=1):
    print(indice, item)