# Praticando if else. Mostrando o maior e menor valor entre três números digitados pelo usuário

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O MENOR valor é {}'.format(menor))
print('O MAIOR valor é {}'.format(maior))
