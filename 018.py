#Verificando se existe "Santo" no nome da pessoa.
# Consertando o espaço e letras maiúsculas que possivelmente o usurario vai colocar

nome = str(input('Digite seu nome todo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
