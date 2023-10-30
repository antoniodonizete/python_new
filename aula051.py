'''
Introdução ao Desenpacotamento + tuples - tuplas

'''
nomes = ['Maria', 'Luiz', 'Helena']

print(nomes)

nome1, nome2, nome3 = nomes
print(nome2)
print(nome3)
print(nome1)

nome1, *resto = ['antonio', 'donizete', 'silva', 777] # *cria variavel com o restante 
#que não será usadoo, e por ser substituido por _ caso o resto seja desprezado
nome1, *_ = ['antonio', 'donizete', 'silva', 777]
print(nome1)
print(resto)

_, nome2, *_ = ['antonio', 'donizete', 'silva', 777] #desprezando o primeiro valor
print(nome2)
print(_)