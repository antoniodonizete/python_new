"""
Repetições
while (enquanto)
Executa uma ação enquanto um condição for --> VERDADEIRA -- True
"""
contador = 0

while contador <= 50:
   contador += 1
   
   if contador == 6:
      print('Não mostrar o', contador)

   if contador >= 10 and contador <= 20:
      print("Não mostrar o", contador)
      continue
   print(contador)   

   if contador == 50:   
      break
 
print('Acabou')