#programa que retorna o aumento de 15% do salário de um funcionário
salario = float(input("Digite seu salário: R$:"))
aumento = salario + (salario * 15/100 )
print('Você recebeu um aumento de 15%. Seu salário atual é de R$: {}' .format(aumento))
