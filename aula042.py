'''
frase = 'O Python é um Linguagem de programação '\
'multiparadgigma. '\
'Python foi criado por Guido van Rossum.'


print(frase.count('o')) # count quantas vezes aparece a palavra Python aparece na frase.
'''
frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtde_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtde_atual:
        qtd_apareceu_mais_vezes = qtde_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
