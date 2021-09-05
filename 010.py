d = int(input("Quantos dias você ficou com carro alugado? "))
km = float(input("Quantos quilometros você andou com carro? "))
totald = d * 60
totalkm = km * 0.15
totalgeral = totald + totalkm
print('O total da diária ficou em R${}. '
      'O total por quilometros rodados ficou em R${}. Seu aluguel ficou em R${}. ' .format(totald, totalkm, totalgeral))
