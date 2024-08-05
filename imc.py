from PySimpleGUI import PySimpleGUI as sg


#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Ínforme seu peso '),sg.Input(key='peso', size=(10, 1))],
    [sg.Text('Informe sua altura'),sg.Input(key='altura', size=(10, 1))],
    [sg.Button('Calcular',), sg.Text('Seu IMC é:'), sg.Output(key='IMCtela')]
]
#janela
janela = sg.Window('Calculo IMC', layout)

#Ler eventos 
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Calcular':
        imc = (float(valores['altura']) *  float(valores['altura'])) / float(valores['peso'])

        print(imc)


