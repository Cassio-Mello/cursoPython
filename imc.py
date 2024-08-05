from PySimpleGUI import PySimpleGUI as sg



#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Ínforme seu peso em Kg(50.0):'),sg.Input(key='peso', size=(10, 1))],
    [sg.Text('Informe sua altura em m(1.9):'),sg.Input(key='altura', size=(10, 1))],
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
    if imc <= 16.9:
        janela['imcCondicao'].update('Muito abaixo do peso!')
    if imc >= 17:
        janela['imcCondicao'].update('Abaixo do peso!')
    if imc >= 18.5:
        janela['imcCondicao'].update('Peso normal!')
    if imc >= 25:
        janela['imcCondicao'].update('Acima do peso!')
    if imc >= 30:
        janela['imcCondicao'].update('Obesidade 1.')
    if imc >= 35:
        janela['imcCondicao'].update('Obesidade 2.')
    if imc > 40:
        janela['imcCondicao'].update('Obesidade 3.')
       



