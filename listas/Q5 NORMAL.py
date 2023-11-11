penteados = input().split(' - ')
tops = input().split(' - ')
bottoms = input().split(' - ')
sapatos = input().split(' - ')
estilos = [penteados, tops, bottoms, sapatos]
posicaoFinal = [-1, -1, -1, -1]

decisao = ''
desistirOFF = True
ameiOFF = True

print('Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!')

while desistirOFF and ameiOFF:
    loopFor = 0
    loopFor -= loopFor
    movimentos = input().split()
    lookFinal = ['', '', '', '']

    print('Iniciando mesclagem...')

    for i in range(len(movimentos)):
        loopFor += 1
        movimentoAtual = movimentos[i]
        direcao = movimentoAtual[-1]
        numMovimentos = int(movimentoAtual[:-1])
        estiloAtual = estilos[i]


        if posicaoFinal[i] == -1:
            posicaoInicial = int(len(estilos[i]) / 2)
        else:
            ultimaPosicao = posicaoFinal[i]
            indicePosicaoFinal = 0
            for indice in range(4):
                if estiloAtual[indice] == ultimaPosicao:
                    indicePosicaoFinal = indice
                    print(f'{estiloAtual}')
                    break
            posicaoInicial = indicePosicaoFinal
            print('========================================================')
            #print(f'Posicao Inicial: {posicaoInicial} de {estiloAtual}')

        # verificacao de tamanho e modificacao do numero de movimentos
        if numMovimentos >= len(estiloAtual):
            numMovimentos = numMovimentos % len(estiloAtual)

        sobraDireita = len(estiloAtual[posicaoInicial + 1:])
        sobraEsquerda = len(estiloAtual[:posicaoInicial])

        if direcao == '>':
            if numMovimentos <= sobraDireita:
                posicaoFinal[i] = estiloAtual[posicaoInicial + numMovimentos]

            elif sobraDireita == 0:
                posicaoFinal[i] = estiloAtual[numMovimentos-1]

            else:
                indiceFinal = numMovimentos - sobraDireita - 1
                posicaoFinal[i] = estiloAtual[indiceFinal]

        else: # direcao == '<':
            if numMovimentos <= sobraEsquerda:
                posicaoFinal[i] = estiloAtual[posicaoInicial - numMovimentos]

            elif sobraEsquerda == 0:
                posicaoFinal[i] = estiloAtual[-(numMovimentos)]

            else:
                posicaoFinal[i] = estiloAtual[-(numMovimentos - sobraEsquerda)]

        lookFinal[i] += posicaoFinal[i]
    print('O look gerado foi:')
    print(f'cabelo {lookFinal[0]}, {lookFinal[1]} com {lookFinal[2]} e {lookFinal[3]} nos pés.')



    decisao = input('')
    if decisao == 'Amei!!':
        if 'camisa da seleção' in lookFinal:
            print('Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!')
        else:
            print('Essa Barbie vai arrasar com o look perfeito!')
        ameiOFF = False

    elif decisao == 'Melhor escolher eu mesma':
        desistirOFF = False
        print('Acho que estou precisando de ajustes, Ken :(')

#123> 12< 324> 123>
#
