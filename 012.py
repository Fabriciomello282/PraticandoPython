# TENTANDO ADIVINHAR QUAL NÚMERO IRÁ APARECER ENTRE 1 E 20. TRABALHANDO COM RANDOM E IF ELSE


import random

n = int(input('Digite um numero e tente acertar o que irá aparecer: '))

numero = random.randint(1, 20)

if n == numero:
  print('PARABÉNS! VOCÊ ACERTOU!!! O NÚMERO É {}' .format(numero))
else:
    print('{} Tente novamente. O número certo é {}' .format(n, numero))
