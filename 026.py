valorcasa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite seu salário R$: ' ))
ano = int(input('Você quer pagar em quantos anos? '))
prestacaomensal = valorcasa / (ano*12)

if prestacaomensal <= salario * (30/100):
    print('Com o valor da casa de R$ {:.2f},'
          ' você terá que pagar R$:{:.2f} por mês em {:.2f} anos!' .format(valorcasa,prestacaomensal, ano))
else:
    print('Empréstimo negado. Seu salário é baixo para o valor dessa casa!')
