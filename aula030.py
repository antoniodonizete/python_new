"""
CONSTANTE = variáveis que não vão mudar
Muita condições no if (ruim)
<-- Contagem de complexidade (ruim)
"""
velocidade = 65 # velocidade atual do carro
local_do_carro = 100 # local em que o carro esá na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde está o radar 1
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar1 = velocidade > RADAR_1
carro_multado_radar1 = local_do_carro >= (
    LOCAL_1 - RADAR_RANGE) and \
        local_do_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar1:
    print('Velocidade carro passou do radar 1.')

if carro_multado_radar1 and \
            vel_carro_pass_radar1:
    print('carro multado em do radar 1.')