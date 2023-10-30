'''
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dols valores oir uma
contagem regressiva iniciando em 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2  
 *  7  4  6  8  2  4  8  9  0 
 = 70 36 48 56 12 20 32 27  0
      
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Muiltiplicar resultado por 10
301 * 10 = 3010
Obter o resto da conta anterior por 11  
3010 % 11 = 7
Se o resultado anterior for maior que 9
    resulto é 0
contrário disso é:
    resultado é o valor da conta
          
     O primeiro dígito do CPF é 7   
               '''
import re
entrada = input('Digite seu CPF: ')
# print(entrada)
# entrada = '74682489070'
entrada = (entrada) \
    .replace('.', '') \
    .replace('-', '') \
    .replace(' ', '') 

entrada = re.sub(
    r'[^0-9]',
    ''
)
# entrada = int(entrada)
cpf = entrada[:9]
nm_conf = [10, 9, 8, 7, 6, 5, 4, 3, 2]
soma_dig1 = 0
i = 0
while i <= 8:
    dig1 = (int(cpf[i]) * nm_conf[i])
    soma_dig1 = (soma_dig1 + dig1)
    i += 1

    resultado = (soma_dig1 * 10) % 11
    novo_digito = resultado if resultado <= 9 else 0

# print(novo_digito)

cpf2 = entrada[:10]
# cpf = '256961388'
nm_conf2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
soma_dig2 = 0
i = 0
while i <= 9:
    dig2 = (int(cpf2[i]) * nm_conf2[i])
    soma_dig2 = (soma_dig2 + dig2)
    i += 1

    resultado2 = (soma_dig2 * 10) % 11
    novo_digito2 = resultado2 if resultado2 <= 9 else 0

print(novo_digito, novo_digito2, sep='')