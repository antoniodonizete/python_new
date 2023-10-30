"""
Iterando strings com while
"""
nome = 'Antonio Donizete' #Iteráveis

n = 0

novo_nome = ''

while n < len(nome):
    letra = nome[n]
    novo_nome += letra
    novo_nome += '*'
    n += 1
novo_nome = '*' + novo_nome
print(novo_nome)






 
print('Fim!')

    
