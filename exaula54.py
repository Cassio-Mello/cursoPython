"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero Inteiro:')

# numero_float = float(numero)
# par_ou_impar = numero_float % 2 == 0
txt_par_ou_impar = 'impar'

try:
    numero_float = float(numero)
    par_ou_impar = numero_float % 2 == 0
    par_ou_impar == True
    txt_par_ou_impar = 'par'
except:
    numero_float == Falses
    print('nada')

    
























"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""