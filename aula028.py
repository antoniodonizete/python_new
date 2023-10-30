"""
Exercício:
Peça ao usuário para dgitar seu nome
Peça ao usuário para dgitar sua idade
Se o nome e idade forem digitados:
    Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe. você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
n = 0
if (nome == '') or (idade == ''):
    print('Desculpe. Você deixou campos vazios.')
    
elif (nome != '') or (idade != ''):
    print('Seu nome é: ',nome)
    print('Seu nome invertido é: ',nome[::-1])
    if (' ' in nome):
        print('Seu nome contém espaços.')    
    elif (' ' not in nome):
        print('Seu nome não contém espaços.') 
    n = (len(nome))   
    print('Seu nome contém', n ,'letras.')    
    print('A primeira letra no seu nome é', nome[0])    
    print('A última a letra no seu nome é', nome[-1])    

