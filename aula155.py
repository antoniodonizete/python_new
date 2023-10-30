# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# import aula154_m
# # from aula154 import soma

# # # print('Este módulo se chama', __name__)
# # # print('Este módulo se chama', __name__)
# # # print(variavel_modulo)
# # print(soma(2, 3))
# # print(aula154.soma(5, 2))

import aula154_m

# print('Este módulo se chama', __name__)
# print(soma(2, 3))
print(aula154_m.soma(5, 2))