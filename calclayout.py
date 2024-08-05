from PySimpleGUI import PySimpleGUI as sg




sg.theme('Reddit')
layout = [
  [sg.Input(key='tela', size=(20,20))],
  [sg.Button('-',size=(3,3)), sg.Button('+',size=(3,3)), sg.Button('/',size=(3,3)), sg.Button('*',size=(3,3))],
  [sg.Button('7',size=(3,3)), sg.Button('8',size=(3,3)),sg.Button('9',size=(3,3))],
  [sg.Button('4',size=(3,3)), sg.Button('5',size=(3,3)),sg.Button('6',size=(3,3))],
  [sg.Button('1',size=(3,3)), sg.Button('2',size=(3,3)),sg.Button('3',size=(3,3))],
  [sg.Button('Calcular'), sg.Button('Apagar'),sg.Button('Sair')]
]
#janela
janela = sg.Window('Calculadora', layout)

numero1 = 0
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == '7':
        numero = eventos
        janela['tela'].update(numero)