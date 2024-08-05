"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra:')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secrerta in palavra_secreta:
        if letra_secrerta in letras_acertadas:
            palavra_formada += letra_secrerta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:

        print('Voce acertou!! PARABENS!')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
    
        sair = input('Quer jogar novamente? [S]im, [N]ao: ').lower().startswith('n')
        if sair is True:
            break