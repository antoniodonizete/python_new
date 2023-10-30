# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras, se uma for falso a expressão inteira será avalida naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None queé usado para representar um não valor
# 
# 
entrada = input('[E]ntrar [S]air: ')
senha_dig = input('Senha: ')

senha_ok = '123456'

if entrada == 'E' and senha_dig == senha_ok:
    print('Entrar')
else:
    print('Sair')   