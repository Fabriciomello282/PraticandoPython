from datetime import date
anoatual = date.today().year
n = int(input('Digite sua data de nascimento: '))
idade = anoatual - n
print('ATLETA COM {} ANOS'.format(idade))

if idade <= 9:
    print('sua categoria é MIRIM')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < idade <= 19:
    print('Sua categoria é JÚNIOR')
elif 19 < idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
