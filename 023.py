viagem = float(input('Digite a distância em KM da viagem que você fará: '))
media = 200

if viagem <= media:
    preço = viagem * 0.5
    print('O valor da sua passagem é de: R${}' .format(preço))
else:
    preço = viagem * 0.45
    print('O valor da sua passagem é de: R${}' .format(preço))

print('Tenha uma excelente viagem!')