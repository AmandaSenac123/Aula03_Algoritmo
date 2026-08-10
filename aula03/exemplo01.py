# GitHub
print('Github - Aula 03')

#Exemplo01 - Veiculo 10 km/1
CONSUMO = 10 # Constante
distancia1 = float(input('Informe a distância: '))
distancia2 = float(input('Informe a outra distância: '))

# Processamento
distancia_total = distancia1 + distancia2
combustivel = distancia_total / CONSUMO

# Saída

print (f'Distância percorrida {distancia_total}')
print (f'Consumo de {combustivel}')
