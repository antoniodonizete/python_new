# Operadores lógicos
# and (e) or (ou) not (não)
# or - Uma das condições precisa ser verdadeiras, se uma for verdadeira a expressão inteira será avalida naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None queé usado para representar um não valor
# # 
entrada = input('[E]ntrar [S]air: ')
senha_dig = input('Senha: ')

senha_ok = '123456'

if (entrada == 'E' or entrada == 'e') and senha_dig == senha_ok:
    print('Entrar')
else:
    print('Sair')    