'''
texto = 'Python'

i = 0
tamanho_da_string = len(texto)

while i < tamanho_da_string:
    print(texto[i], i)

    i += 1
     '''   
texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(f'{novo_texto}*')
