"""
Repetições
while (enquanto)
Executa uma ação enquanto um condição for --> VERDADEIRA -- True
"""
condicao = True

while condicao:
    nome = input('Digite se nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou!')