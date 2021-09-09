# TENTANDO ADIVINHAR QUAL NÚMERO
# IRÁ APARECER ENTRE 0 E 5. TRABALHANDO COM RANDOM, IF ELSE
from random import randint
n = int(input('Digite um numero e tente acertar o que irá aparecer: '))

numero = randint(0, 5)

if n == numero:
  print('PARABÉNS! VOCÊ ACERTOU!!! O NÚMERO É {}' .format(numero))
else:
    print('{} Tente novamente. O número certo é {}' .format(n, numero))
