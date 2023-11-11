#aranha
nomeAranha = input()
ataqueAranha = int(input())
defesaAranha = int(input())
#aliado
nomeAliado  = input()
ataqueAliado = int(input())
defesaAliado = int(input())
#vilao
nomeVilao = input()
ataqueVilao = int(input())
defesaVilao = int(input())
#capanga
nomeCapanga = input()
ataqueCapanga = int(input())
defesaCapanga = int(input())
#fator sorte
fatorSorte_1 = int(input())
fatorSorte_2 = int(input())
fatorSorte_3 = int(input())

vitoriasAranha = 0
vitoriasVilao = 0

#ordem de ataques: no primeiro o ''aranha'' ataca, no segundo confronto o ''vilão'' ataca e no 3º o ''aranha'' ataca novamente
#sorte: 0-todos sozinhos    >=                         1-atacante ataca com seu parceiro  analisar
#sorte: 2-defensor defende com seu parceiro   analise       3-ambos atacam e defendem com seus respectivos parceiros    >=

#===================================================================
#PRIMEIRO ROUND          CAPANGA DEFENDE / MIRANHA ATACA
print('1° confronto:')
#===================================================================
#SORTE 0
if fatorSorte_1 == 0:
    if ataqueAranha >= defesaVilao:
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
#SORTE 1
elif fatorSorte_1 == 1:
    if (ataqueAranha + ataqueAliado) >= defesaVilao:
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
#SORTE 2
elif fatorSorte_1 == 2:
    if ataqueAranha > (defesaCapanga + defesaVilao):
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
#SORTE 3
elif fatorSorte_1 == 3:
    if (ataqueAranha + ataqueAliado) >= (defesaVilao + defesaCapanga):
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
#SEGUNDO ROUND          CAPANGA ATACA / MIRANHA DEFENDE
print('2° confronto:')
#===================================================================
#SORTE 0
if fatorSorte_2 == 0:
    if defesaAranha >= ataqueVilao:
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
        vitoriasVilao += 1
#===================================================================
#SORTE 1
elif fatorSorte_2 == 1:
    if fatorSorte_2 == 1:
        if defesaAranha > (ataqueVilao + ataqueCapanga):
            print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
            vitoriasAranha += 1
        else:
            print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
            vitoriasVilao += 1
#===================================================================
#SORTE 2
elif fatorSorte_2 == 2:
    if (defesaAranha + defesaAliado) >= ataqueVilao:
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
        vitoriasVilao += 1
#===================================================================
#SORTE 3
elif fatorSorte_2 == 3:
    if (defesaAranha + defesaAliado) >= (ataqueVilao + ataqueCapanga):
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
        vitoriasVilao += 1
#===================================================================
#TERCEIRO ROUND          CAPANGA DEFENDE / MIRANHA ATACA
print('3° confronto:')
#===================================================================
#SORTE 0
if fatorSorte_3 == 0:
    if ataqueAranha >= defesaVilao:
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
#SORTE 1
if fatorSorte_3 == 1:
    if (ataqueAranha + ataqueAliado) >= defesaVilao:
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
#SORTE 2
if fatorSorte_3 == 2:
    if ataqueAranha > (defesaVilao + defesaCapanga):
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
#SORTE 3
if fatorSorte_3 == 3:
    if (ataqueAranha + ataqueAliado) >= (defesaVilao + defesaCapanga):
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
        vitoriasAranha += 1
    else:
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
        vitoriasVilao += 1
#===================================================================
if vitoriasAranha > vitoriasVilao:
    print(f'O {nomeAranha} e {nomeAliado} conseguiram derrotar o {nomeVilao} e recuperar o multiverso!')
else:
    print(f'O {nomeVilao} e {nomeCapanga} invadiram Nova York, onde estão os outros aranhas??')
#===================================================================
