#Iterando strings com while
#      01234567891011
nome = 'Çassio Mello'



indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'    
    
    indice += 1
    print(novo_nome)