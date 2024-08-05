#Criar uma calculadora que faca calculos com dois numeros os calculos podem ser +-*/



#utilizando while para criar um loop
while True:
   #coletando os numeros
    numero_1 = input('Insira um numero:')
    operador_matematico = input('Insira um operador (-+*/):')
    numero_2 = input('Inssira outro numero:')
    

    #criando um flag para checar se os numeros sao validos
    numero_valido = None

    #usando funcao try execpt para checar se os numero sao validos
    try:
        #convertendo numeros para float
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
    
        numero_valido = True
    except:
        numero_valido = None
    #condicionando se o numero nao for valido e exibindo msg
    if numero_valido is None:
        print('Um ou ambos os numeros nao sao validos')
        continue
    
    #operadores permitidos
    operadores = '-+*/'
    
    #conferindo se o operador é valido
    if operador_matematico not in  operadores:
        print('Digite um operador valido!')
        continue

    #conferindo se foi digitado apenas um operador matematico
    if len(operador_matematico) > 1:
        print('Digite apenas 1 operador!')
        continue
    
    #calculando subtracao
    if operador_matematico == '-':
        resultado_subtracao = numero_1_float - numero_2_float
        print(f'Resultado de: {numero_1} - {numero_2} = {resultado_subtracao:.2f}')
        
    #calculando adicao
    if operador_matematico == '+':
        resultado_adicao = numero_1_float + numero_2_float
        print(f'Resultado de: {numero_1} + {numero_2} = {resultado_adicao:.2f}')
    
    #calculando multiplicacao
    if operador_matematico == '*':
        resultado_multiplicacao = numero_1_float * numero_2_float
        print(f'Resultado de: {numero_1} * {numero_2} = {resultado_multiplicacao:.2f}')
    
    #calculando divisao
    if operador_matematico == '/':
        resultado_divisao = numero_1_float / numero_2_float
        print(f'Resultado de: {numero_1} / {numero_2} = {resultado_divisao:.2f}')

    
    
    sair = input('Quer sair? [s]air:').lower().startswith('s')

    if sair is True:
        break