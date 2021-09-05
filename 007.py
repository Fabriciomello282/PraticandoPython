#CALCULANDO QUANTO DE TINTA VAMOS USAR PARA PINTAR UMA PAREDE
# POR METROS QUADRADOS

alt = float(input('Digite a altura da sua parede: '))
larg = float(input('Digite a largura de sua parede: '))
area = larg * alt
print('sua parede tema dimensão de {}x{} e a área é de {}m²' .format(alt, larg, area))

tinta = area/2

print('para pintar a parede você vai precisar de {} litros de tinta' . format(tinta))