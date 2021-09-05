valor = float(input('Digite o valor do poduto: R$'))
desc = valor * 5/100
pag = valor - desc
print('vc ganhou R${} com o desconto de 5% e vai pagar apenas R${}' .format(desc, pag))