"""Calculadora com while"""

while True:
    numero_1 = input('Digite um número: ')
    operador = input('Digite o operador (+-/*): ')
    numero_2 = input('Digite outro número: ')

   
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
   
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True       
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido.') 
        continue
    
    if len(operador) < 1:
        print('Digite apemas 1 operador.')
        continue
    
    print('O Resultado da sua conta é:')

    if operador =='+':
        print(num_1_float + num_2_float)
    elif operador =='-':
        print(num_1_float - num_2_float)
    elif operador =='*':
        print(num_1_float * num_2_float)
    elif operador =='/':
        print(num_1_float / num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    if sair is True:
        break
