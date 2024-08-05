#Calcular Média


nota_1 = input('Inssira a primeira nota:')
nota_2 = input('Inssira a segunda nota:')
nota_3 = input('Inssira a terceira nota:')
nota_4 = input('Inssira a quarta nota:')

float_nota1 = float(nota_1)
float_nota2 = float(nota_2)
float_nota3 = float(nota_3)
float_nota4 = float(nota_4)

numero_de_notas = 4 

media = (float_nota1 + float_nota2 + float_nota3 + float_nota4) / numero_de_notas

print('Sua média é:', media)
if media >=6 :
    print('voce foi APROVADO')
else :
    print('voce foi REPROVADO')
