"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'perfume'
# completar = len(palavra_secreta)
palavra_digitada = ''
letra_digitada = ''
i = ''

while palavra_digitada != palavra_secreta:    
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('Digite apenas 1 letra!')
        continue
    if letra_digitada not in palavra_secreta[:]:
        print(f'A palavra secreta não contém a letra "{letra_digitada}".' )
        continue
    if letra_digitada in palavra_secreta[:]:
        palavra_digitada = palavra_digitada + letra_digitada
        if len(palavra_digitada) < len(palavra_secreta):
            print(f'{palavra_digitada}',(len(palavra_secreta) - len(palavra_digitada))*'*')
            print(f'{letra_digitada}'in palavra_secreta)
        
    