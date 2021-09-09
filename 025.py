salario = float(input('Digite o seu salário R$: '))
if salario <= 1250:
    salarioatual = salario + (salario * 15/100)
    print('Você recebeu um aumento de 15% e seu salário atual é de R${} ' .format(salarioatual))
else:
    salarioatual = salario + (salario * 10/100)
    print(' Você recebeu um aumento de 10% e seu salário atual é de R${} ' .format(salarioatual))