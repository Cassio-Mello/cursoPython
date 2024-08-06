from PySimpleGUI import PySimpleGUI as sg




sg.theme('Reddit')
layout = [
  [sg.Input(key='tela', size=(22,20))],
  [sg.Button('-',size=(3,3)), sg.Button('+',size=(3,3)), sg.Button('/',size=(3,3)), sg.Button('*',size=(3,3))],
  [sg.Button('7',size=(3,3)), sg.Button('8',size=(3,3)),sg.Button('9',size=(3,3)), sg.Button('(', size=(3,3))], 
  [sg.Button('4',size=(3,3)), sg.Button('5',size=(3,3)),sg.Button('6',size=(3,3)), sg.Button(')', size=(3,3))],
  [sg.Button('1',size=(3,3)), sg.Button('2',size=(3,3)),sg.Button('3',size=(3,3)),sg.Button('0',size=(3,3))],
  [sg.Button('Calcular'), sg.Button('Apagar'),sg.Button('<--', size=(3))]
]
#janela
janela = sg.Window('Calculadora', layout)

numero1 = ''
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == '1':
        numero1 +='1'
        janela['tela'].update(numero1)

    if eventos == '2':
        numero1 += '2'
        janela['tela'].update(numero1)

    if eventos == '3':
        numero1 +='3'
        janela['tela'].update(numero1)

    if eventos == '4':
        numero1 +='4'
        janela['tela'].update(numero1)

    if eventos == '5':
        numero1 +='5'
        janela['tela'].update(numero1)

    if eventos == '6':
        numero1 +='6'
        janela['tela'].update(numero1)

    if eventos == '7':
        numero1 +='7'
        janela['tela'].update(numero1)

    if eventos == '8':
        numero1 +='8'
        janela['tela'].update(numero1)

    if eventos == '9':
        numero1 +='9'
        janela['tela'].update(numero1)

    if eventos == '0':
        numero1 +='0'
        janela['tela'].update(numero1)

    if eventos == '-':
        numero1 +='-'
        janela['tela'].update(numero1)

    if eventos == '+':
        numero1 +='+'
        janela['tela'].update(numero1)

    if eventos == '/':
        numero1 +='/'
        janela['tela'].update(numero1)

    if eventos == '*':
        numero1 +='*'
        janela['tela'].update(numero1)

    if eventos == '(':
        numero1 +='('
        janela['tela'].update(numero1)

    if eventos == ')':
        numero1 +=')'
        janela['tela'].update(numero1)

    if eventos == 'Calcular':
        resultado = eval(numero1)
        janela['tela'].update(resultado)

    if eventos == 'Apagar':
        numero1 =''
        janela['tela'].update(numero1)
    if eventos == '<--':
        tamanho = len(numero1)
        apagar = tamanho - 1
        numero1 = numero1[slice(apagar)]
        janela['tela'].update(numero1)       

        
        
        

    
        