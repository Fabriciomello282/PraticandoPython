frase = str(input('Digite uma frase: ')).strip().lower()
print('Sua frase tem {} Letras "a" '.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {}' .format(frase.find('a')+1))
print('A ultima letra A apareceu na posição {}' .format(frase.rfind('a')+1))