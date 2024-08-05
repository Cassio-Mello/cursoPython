#Hash tag permite escrever comentarios 
"""
Isso nao comentario como cerquilha
isso e chamado de DocString
onde posso escrever qualquer coisa em
multi linha
"""
'''
tambem pode ser usssado com 3 aspas simplas
neses casos o interpretador nao igonora as linha
ele as le mas nao faz nada com elas
'''
numero = 10    
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')