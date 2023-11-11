#Se o número for par ((dica/2)**(1/2)) + 2
#Se o número for ímpar (dica/3) + 3
frase_dita = False
dc_on = False

dica = int(input())

if dica%2 == 0:
    dica = ((dica/2)**(0.5)) + 2

elif dica%2 != 0:
    dica = (dica/3) + 3

filme_1 = input()
filme_2 = input()
filme_3 = input()

if filme_1 == 'Batman vs Superman' or filme_1 == 'Coringa' or filme_1 == 'O Cavaleiro das Trevas':
    dc_on = True

cansaco = 0

if filme_1 == 'Vingadores: Ultimato':
    cansaco += 2
else:
    cansaco += 1
#filme 1
if dc_on == False:
    if frase_dita == False:
        if len(filme_1) == dica:
            print('Miles: Achei o easter egg!!!')
            frase_dita = True
            filme_4 = input()
            duracao_4 = int(input())

            if cansaco >= 2 and duracao_4 >= 135:
                print('Miles: A mimir')
            elif cansaco >= 2 and 120 <= duracao_4 and duracao_4 < 135:
                print('Gwen: Nada que uma xícara de café não resolva!')
            elif duracao_4 < 120 or cansaco < 2:
                print(f'Peter: {filme_4} é o melhor filme do homem aranha, 10/10')

if dc_on == False:
    if frase_dita == False:
        print('Miles: Tou frio, melhor ir procurar nas fases mais antigas')
#===============================================
if filme_2 == 'Vingadores: Ultimato':
    cansaco += 2
else:
    cansaco += 1
#===============================================
#filme 2
if dc_on == False:
    if frase_dita == False:
        if len(filme_2) == dica:
            print('Miles: Achei o easter egg!!!')
            frase_dita = True
            filme_4 = input()
            duracao_4 = int(input())
            if cansaco >= 2 and duracao_4 >= 135:
                print('Miles: A mimir')
            if cansaco >= 2 and 120 <= duracao_4 and duracao_4 < 135:
                print('Gwen: Nada que uma xícara de café não resolva!')
            if duracao_4 < 120:
                print(f'Peter: {filme_4} é o melhor filme do homem aranha, 10/10')

if dc_on == False:
    if frase_dita == False:
        print('Gwen: Cadê o velho??? Queria um autógrafo')
#===============================================
if filme_3 == 'Vingadores: Ultimato':
    cansaco += 2
else:
    cansaco += 1
#===============================================
#filme 3
if dc_on == False:
    if frase_dita == False:
        if len(filme_3) == dica:
            print('Miles: Achei o easter egg!!!')
            frase_dita = True
            filme_4 = input()
            duracao_4 = int(input())
            if cansaco >= 2 and duracao_4 >= 135:
                print('Miles: A mimir')
            if cansaco >= 2 and 120 <= duracao_4 and duracao_4 < 135:
                print('Gwen: Nada que uma xícara de café não resolva!')
            if duracao_4 < 120:
                print(f'Peter: {filme_4} é o melhor filme do homem aranha, 10/10')

if dc_on == False:
    if frase_dita == False:
        print('Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...')

if dc_on == True:
    print('Algo de errado não está certo!')