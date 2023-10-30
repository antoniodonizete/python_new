'''
split e join com list e str
split - divid uma string
join - une uma string
'''
frase = 'olha só que, coisa interessante'
lista_palavra = frase.split(', ') # se deixar vazio divide pelo espaço em branco
lista_palavra1 = frase.split(',') # indica caracter para dividir
lista_palavra2 = frase.split(', ') # indica caracter para dividir 
print(frase)
print(lista_palavra)
print(lista_palavra1)
print(lista_palavra2)
for i, frase in enumerate(lista_palavra):
    print(lista_palavra[i])