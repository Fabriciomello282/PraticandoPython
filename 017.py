#O nome da cidade tem que começar com 'SANTO' para dar verdadeiro;

cidade = str(input('informe o local que voce mora: ')).strip()
print(cidade[:5].upper() == 'SANTO')
