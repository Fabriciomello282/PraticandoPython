#SENO COSSENO E TANGENTE DE UM ANGULO - trabalhando com biblioteca
from math import radians, tan, sin, cos
angulo = float(input('Digite o Angulo desejado: '))
seno = sin(radians(angulo))
print('O ângulo {} tem o seno de {:.2f}' .format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo {} tem o COSSENO de {:.2f}' .format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo {} tem a TANGENTE de {:.2f}' .format(angulo, tangente))


