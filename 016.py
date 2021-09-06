nome = str(input('Digite seu nome completo: ')).strip()
print('seu nome em maiusculo é {}' .format(nome.upper()))
print('seu nome em minusculo é {}' .format(nome.lower()))
print('seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
