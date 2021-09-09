numero = int(input('Digite um número inteiro: ' ))
escolha = int(input('''Escolha a conversão desejada:
                    [1] Binária 
                    [2] Octal 
                    [3] Hexadecimal '''))
if escolha == 1:
    print('{} convertido em binário fica {} ' .format(numero, bin(numero)[2:]))
elif escolha ==2:
    print('{} convertido para Octal fica {}' .format(numero, oct(numero)[2:]))
elif escolha ==3:
    print('{} convertido para Hexadecimal fica {}' .format(numero, hex(numero)[2:]))
else:
    print('Faça novamente e escolha uma das opções apresentadas!')
