time_1 = input('')
time_2 = input('')

vitorias_1 = 0
vitorias_2 = 0

contador = 0
condicao_booleana = True

while (vitorias_1 <= 2 or vitorias_2 <= 2) and condicao_booleana == True:

    pontuacao_1 = int(input())
    pontuacao_2 = int(input())

    if pontuacao_1 > pontuacao_2:
        vitorias_1 += 1
        contador += 1
        print(f'O vencedor da {contador}ª rodada foi: {time_1}')
    elif pontuacao_2 > pontuacao_1:
        vitorias_2 += 1
        contador += 1
        print(f'O vencedor da {contador}ª rodada foi: {time_2}')

    if vitorias_1 == 3:
        print(f'O time {time_1} ganhou a partida final!')
        condicao_booleana = False
    elif vitorias_2 == 3:
        print(f'O time {time_2} ganhou a partida final!')
        condicao_booleana = False
