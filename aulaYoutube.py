numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novo_numeros = [numero for numero in numeros if numero > 5]
impares = [numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
novo_numeros = [numero for numero in numeros if numero > 5]
outro_numero = [
    numero 
    if numero != 6
    else '$$$'
    for numero in numeros if numero % 2 == 0]

print(numeros)
print(f'Impares:', impares)
print(f'Pares:', pares)
print(novo_numeros)
print(f'Outro:', outro_numero)
