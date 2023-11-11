#MONTAR TIME COM OU SEM PARTICIPANTES
#AVALIAR SE VAI VENCER O TIME JA MONTADO
#BRUNA CRASHA A MONTAGEM
#ARTUR PERDE INDEPENDENTE DA QUANTIDADE DE PONTOS
#FREJ VENCE INDEPENDENTE DA QUANTIDADE DE PONTOS
#SE FREJ E ARTUR ESTIVEREM NA MESMA EQUIPE, OS EFEITOS SAO ANULADOS E A CONTAGEM OCORRE NORMALMENTE
nome = ''
posicao = ''
elo = ''

nome1 = ''
posicao1 = ''
elo1 = ''

nome2 = ''
posicao2 = ''
elo2 = ''

nome3 = ''
posicao3 = ''
elo3 = ''

nome4 = ''
posicao4 = ''
elo4 = ''

nome5 = ''
posicao5 = ''
elo5 = ''

pontosEquipe = 0

time = 0
brunaOFF = True
arturON = False
frejON = False
timeFechado = False
novoIntegrante = False

playerDOIS = False
playerTRES = False
playerQUATRO = False


while not timeFechado and brunaOFF:
    time += 1
    nomeInput = input()
    if nomeInput == 'Bruna':
        print('LOL NÃO!!! TUDO MENOS LOL!!!')
        brunaOFF = False
    if brunaOFF:
        posicaoInput = input()
        eloInput = input()
        nome += nomeInput
        posicao += posicaoInput
        elo += eloInput


    #========================================================================
        if elo != 'Bronze' and elo != 'Prata' and elo != 'Ouro' and elo != 'Platina' and elo != 'Diamante' and elo != 'Desafiante':
            print('Não conheço esse elo, então vou considerar que é um elo ruim.')


        if time == 1:
            print(f'{nome} entrou pro time.')
            nome1 = nome
            posicao1 = posicaoInput
            elo1 = eloInput
            novoIntegrante = True

        elif time == 2:
            if posicao != posicao1:
                print(f'{nome} entrou pro time.')
                nome2 = nome
                posicao2 = posicaoInput
                elo2 = eloInput
                playerDOIS = True
                novoIntegrante = True
            else:
                print(f'{nome} não foi aceito, que pena.')
                if not playerDOIS:
                    nome2 = ''
                    posicao2 = ''
                    elo2 = ''
                time -= 1

        elif time == 3:
            if posicao != posicao1 and posicao != posicao2:
                print(f'{nome} entrou pro time.')
                nome3 = nome
                posicao3 = posicaoInput
                elo3 = eloInput
                novoIntegrante = True
                playerTRES = True
            else:
                print(f'{nome} não foi aceito, que pena.')
                if not playerTRES:
                    nome3 = ''
                    posicao3 = ''
                    elo3 = ''
                time -= 1

        elif time == 4:
            if posicao != posicao1 and posicao != posicao2 and posicao != posicao3:
                print(f'{nome} entrou pro time.')
                nome4 = nome
                posicao4 = posicaoInput
                elo4 = eloInput
                playerQUATRO = True
                novoIntegrante = True
            else:
                print(f'{nome} não foi aceito, que pena.')
                if not playerQUATRO:
                    nome4 = ''
                    posicao4 = ''
                    elo4 = ''
                time -= 1

        elif time == 5:
            if posicao != posicao1 and posicao != posicao2 and posicao != posicao3 and posicao != posicao4:
                print(f'{nome} entrou pro time.')
                nome5 = nome
                posicao5 = posicaoInput
                elo5 = eloInput
                novoIntegrante = True
                timeFechado = True
            else:
                print(f'{nome} não foi aceito, que pena.')
                nome5 = ''
                posicao5 = ''
                elo5 = ''
                time -= 1

        if novoIntegrante:
            if elo == 'Bronze':
                pontosEquipe += 1
            elif elo == 'Prata':
                pontosEquipe += 2
            elif elo == 'Ouro':
                pontosEquipe += 4
            elif elo == 'Platina':
                pontosEquipe += 6
            elif elo == 'Diamante':
                pontosEquipe += 8
            elif elo == 'Desafiante':
                pontosEquipe += 10



        if nome == 'Artur':
            print('Ele tá meio enferrujado...')
            arturON = True
        elif nome == 'Frej':
            print('Joga muito!')
            frejON = True

        if time == 5 and novoIntegrante:
            print('O time está completo.')
            print(f"{nome1} - {posicao1} ({elo1})")
            print(f"{nome2} - {posicao2} ({elo2})")
            print(f"{nome3} - {posicao3} ({elo3})")
            print(f"{nome4} - {posicao4} ({elo4})")
            print(f"{nome5} - {posicao5} ({elo5})")

            if not arturON and frejON:
                print('A GENTE VAI GANHAR!!!')
                pontosEquipe = 100
            elif not frejON and arturON:
                print("Vai dar ruim...")
                pontosEquipe = 0
            elif not frejON and not arturON:
                if pontosEquipe >= 18:
                    print('A GENTE VAI GANHAR!!!')
                else:
                    print("Vai dar ruim...")
            elif arturON and frejON:
                if pontosEquipe >= 18:
                    print('A GENTE VAI GANHAR!!!')
                else:
                    print("Vai dar ruim...")
            #print(frejON)
            #print(arturON)

    novoIntegrante = False
    nome = ''
    posicao = ''
    elo = ''
