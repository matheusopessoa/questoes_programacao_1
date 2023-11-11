loops = 0
rodadas = int(input())
pontuacao_Manchester = 0
pontuacao_Spi = 0
neg = False

while loops < rodadas and not neg:
    time = input('')
    gols = int(input())
    chutes = int(input())
    amarelos = int(input())
    vermelhos = int(input())

    if time == 'Manchester CIn':
        pontuacao_Manchester += (gols*10) + (chutes*3) + (amarelos*-2) + (vermelhos*-4)
        if gols >= 0.3 * chutes:
            pontuacao_Manchester += 3
        if vermelhos >= amarelos:
            pontuacao_Manchester -= 3

    elif time == 'SpiCIn Girls':
        pontuacao_Spi += (gols*10) + (chutes*3) + (amarelos*-2) + (vermelhos*-4)
        if gols >= 0.3 * chutes:
            pontuacao_Spi += 3
        if vermelhos >= amarelos:
            pontuacao_Spi -= 3
    loops += 1
    if pontuacao_Spi < 0 or pontuacao_Manchester < 0:
        neg = True

total = pontuacao_Manchester + pontuacao_Spi
porcentagem_Manchester = 100*(pontuacao_Manchester/total)
porcentagem_Spi = 100*(pontuacao_Spi/total)

if pontuacao_Spi < 0:
    print(f'O time SpiCIn Girls ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.')
elif pontuacao_Manchester < 0:
    print(f'O time Manchester CIn ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.')

elif porcentagem_Spi > porcentagem_Manchester:
    print(f'Com {porcentagem_Spi:.2f}% dos pontos, o time SpiCIn Girls pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')

else:
    print(f'Com {porcentagem_Manchester:.2f}% dos pontos, o time Manchester CIn pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')
