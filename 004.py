#TREINANDO E ENTENDENDO O .IS

a = input('digite um numero: ')
print('Seu tipo primitivo é ', type(a))
print('só tem espaços? ', a.isspace())
print('É um número ', a.isnumeric())
print('É alfabético ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo? ', a.islower())
print('Está captalizada? ', a.istitle())