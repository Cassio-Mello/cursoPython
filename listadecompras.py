'''
faça umalista de compras com listas
o ususario pode apapgar, listar e visualizar sua lista
nao permita quebug
'''



listaCompras = []


while  True:
    opcao = input('Escolha um opção:\n[I]nserir    [E]xcluir    [V]ver lista   [S]sair\n').lower()

    if opcao == 'i':

        listaCompras.append(input('Adicione um item:\n'))
        print(f'{listaCompras} foi adicionado a su lista de compras!')
        
    elif opcao =='v':
       for indice, nome in enumerate(listaCompras):
           print(indice,nome)
       
    elif opcao =='e':
        excluir = int(input('Informe qual item deseja excluir:'))

        if excluir > len(listaCompras):
            print('O item nao existe')

        try:
            exluir = int(excluir)
            del listaCompras[excluir]
        except:
            print('Informe um numero inteiro!')


    elif  opcao == 's':
        break
   
   
   
   




