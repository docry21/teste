# Distância entre Ribeirão Preto e Franca
distancia = int(input("digite a distancia em km: "))  # km

# Velocidade do carro e do caminhão
velocidadocarro = 110  # km/h
velocidadocaminhao = 80  # km/h

# Distância percorrida por cada veículo até o ponto de encontro
distanciacarro = distancia / 2
distanciacaminhao = distancia / 2

# Tempo que cada veículo leva para percorrer a distância até o ponto de encontro
tempocarro = distanciacarro / velocidadocarro
tempocaminhao = distanciacaminhao / velocidadocaminhao

# Comparação dos tempos para determinar qual veículo está mais próximo de Ribeirão Preto
if tempocarro < tempocaminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")
