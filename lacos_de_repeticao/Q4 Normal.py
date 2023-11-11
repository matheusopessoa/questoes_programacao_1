equipe1_nome1 = input()
equipe1_nome2 = input()
equipe2_nome1 = input()
equipe2_nome2 = input()
quantidade_partidas = int(input())

loop = 0

notDesistencia = True

print(f'VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:')
print(f'{equipe1_nome1} e {equipe1_nome2} X {equipe2_nome1} e {equipe2_nome2}')

vitorias1 = 0
vitorias2 = 0

pontosTotais1 = 0
pontosTotais2 = 0

while loop < quantidade_partidas and notDesistencia:
    loop += 1

    pontuacao1 = int(input())
    pontuacao2 = int(input())
    pontosTotais1 += pontuacao1
    pontosTotais2 += pontuacao2

    if pontuacao1 == 0 or pontuacao2 == 0:
        if pontuacao1 == 0 and pontuacao1<pontuacao2:
            print('JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA')
            notDesistencia = False
        elif pontuacao2 == 0 and pontuacao2<pontuacao1:
            print('JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA')
            notDesistencia = False
    else:
        if pontuacao1 >= pontuacao2:
            vitorias1 += 1
        elif pontuacao1 < pontuacao2:
            vitorias2 += 1


if notDesistencia:
    print(f'CARAMBA! Tivemos um total de {pontosTotais1 + pontosTotais2} bolas ao chão ao longo dessa disputa.')
    coenf1 = pontosTotais1 * (vitorias1/quantidade_partidas)
    coenf2 = pontosTotais2 * (vitorias2 / quantidade_partidas)
    if coenf1 >= coenf2:
        print(f'{equipe1_nome1} e {equipe1_nome2} são os grandes vencedores!')
        print(f'Mataram {pontosTotais1} bolas, ganhando {vitorias1} partidas')
    elif coenf2 > coenf1:
        print(f'{equipe2_nome1} e {equipe2_nome2} são os grandes vencedores!')
        print(f'Mataram {pontosTotais2} bolas, ganhando {vitorias2} partidas')




