
'''
for i in range(''):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
'''
texto = 'abcde'
qt_ltt = len(texto)
qt_lt = int(qt_ltt)
i = 'e'
for i in texto:
#   if i == 2:
    print(f'{i:*^5}')
    continue
#print(f'{variavel:*^11}')
    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')