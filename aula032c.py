"""157825
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário  não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
num = input('Digite um número inteiro: ')
try:
    num_int = int(num)
    if num_int % 2 == 0:
        print('Este número é par.')
    else:
        print('Este número é impar.')
except:
      print('Este não é um número inteiro.')
"""      
"""
Faça um programa que pergunte ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""
'''
hora_comp = input('Digite as horas: ')
hora_conv = hora_comp[0 : 2]
hora = (int(hora_conv))
if hora <= 11:
    print('Bom dia')
if  (hora >= 12) and (hora <= 17):
    print('Boa tarde')
if  (hora >= 18) and (hora <= 23):
    print('Boa noite') 

'''
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 letras "Seu nome é muito grande"
"""

name = input('Digite seu nome: ')
total_letras = (len(name))
if total_letras <= 4:
    print('Seu nome é curto.')
elif total_letras <= 6:
    print('Seu nome é normal.')
elif total_letras >= 7:
    print('Seu nome é muito grande')

