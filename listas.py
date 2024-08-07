"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: 
        append -Adiciona um item ao final
        insert - Adiciona um item no Indice escolhido
        pop - Remove do final ou do indice escolhido
        del - apaga um indice 
        clear - limpa a lista 
        extend - estende a lista
        + - concatena listas
        Create Read Update  Delete
        criar  ler  alterar apagar = lista[i] (CRUD)
"""
#lista = [123, True, 'Cássio Mello', 1.2, []] esta sempre entrecolchetes

# lista = [10, 20, 30, 40]
# print(lista)
# lista[2] = 300
# print(lista)
# del lista[2] #deletendo indice 2
# print(lista)
# lista.append(50) #adiciona um valor no final da lista
# lista.append(60)
# lista.append(70)
# lista.pop() #ele apaga o ultimo valor da lista e retorna um valor que pode ser guardado em variavel
# valorPop = lista.pop()
# print(valorPop)
# print(lista)
# lista.insert(0, 100) #o primeiro nuero idica em qual indiceeuquero iserir o segundo é o valor a ser iserido
# print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)