from datetime import date
anoatual = date.today().year

nasc = int(input('Digite o ano que você NASCEU: '))
idade = anoatual - nasc
anoalist = nasc + 18
if idade > 18:
    anoalist = nasc + 18
    print('Você já tem {} anos e deveria ter se alistado em {}!! ' .format(idade, anoalist))
elif idade < 18:
    anoalist = nasc + 18
    print('Você tem {} anos e terá que se alistar em {}'.format(idade, anoalist))
else:
    print('Você tem {} anos e tem que se alistar IMEDIATAMENTE NESSE ANO!' .format(idade))