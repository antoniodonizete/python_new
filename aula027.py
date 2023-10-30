"""
 Fatiamento de string
 012345678
 Olá Mundo
-987654321

Fetiamento [i:f:p] inicio/fim/passo padrão 1 em 1 [::]
Obs.: a função len retorna a qtd de
caracteres da string
"""

variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(len(variavel))
print(len(variavel[0:4]))
print(variavel[0:9:2])
print(variavel[::-1]) #inverte 
print(variavel[-1:-10:-1]) #inverte
