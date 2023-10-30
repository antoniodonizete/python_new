'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores de sua listas
não permita que o programa quebre com erros ou 
indices inexistentes na lista.
'''
import os
lista = []
inserir = 'i'
apagar = 'a'
listar = 'l'


while ...:    
    print('Selecione uma opção válida' )
    opcao = input('[a]pagar [i]nserir [l]istar: ')

    if opcao == inserir:
        it_insert = input('Digite o item a inserir: ')
        lista.append(it_insert)
        print(f'Item {it_insert} inserido na lista.')
    #     lista.append()


    if opcao == apagar: 
        for indice, item in enumerate(lista):
            print(indice, item)
        it_del = input('Digite o numero item a apagar: ')
        it_del = int(it_del)
        del lista[it_del]
        print('item apagado')

    if opcao == listar:
        for indice, item in enumerate(lista):
            print(indice, item)
        # for indice in lista:
        #     indice, item = lista
        #     print(indice, item)
    # if opcao != listar and apagar and inserir: 
    #     print('Opção inválida')

    continue