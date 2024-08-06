texto = '123456'

tamanho = len(texto)
print(tamanho)
apagar = tamanho - 1
print(apagar)

texto = texto[slice(apagar)]

print(texto)