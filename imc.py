from PySimpleGUI import PySimpleGUI as sg



#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Ínforme seu peso em Kg:'),sg.Input(key='peso', size=(10, 1))],
    [sg.Text('Informe sua altura em m:'),sg.Input(key='altura', size=(10, 1))],
    [sg.Button('Calcular',), sg.Text('Seu IMC é:'), sg. Text('', key='valorIMC'), sg.Text('', key='imcCondicao')]
]
#janela
janela = sg.Window('Calculo IMC', layout)

#Ler eventos 
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Calcular':
        imc = float(valores['peso'])/ (float(valores['altura']) *  float(valores['altura']))
        janela['valorIMC'].update(int(imc))
    if imc < 16.9:
        janela['imcCondicao'].update('Muito abaixo do peso')
       



