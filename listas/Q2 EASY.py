itensLevar = input()
levarSplit = itensLevar.split(', ')

itensEncontrados = input()
encontradosSplit = itensEncontrados.split(', ')

numLevar, numEncontrados, achados, loop = len(levarSplit), len(encontradosSplit), 0, 0

frase = False
iguais = False


for item in levarSplit:
    loop += 1

    if item in encontradosSplit:
        achados += 1
        if frase == False:
            print('Esses são os itens que já tenho em casa:')
            frase = True
        print(f'{achados}º item: {item}')

    if loop == (numLevar):
        #ACHOU ALGUNS
        if achados != 0 and not (set(levarSplit).issubset(set(encontradosSplit))):
            if numLevar - achados != 0:
                print(f'Irei precisar comprar {numLevar - achados} itens antes do meu encontro!')
                print('Isso é tudo! Hora de me preparar!')
        #ACHOU NADA
        elif achados == 0:
            print(f'Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {numLevar} itens em casa.')
            print('Isso é tudo! Hora de me preparar!')
        #ACHOU TUDO
        elif iguais == False:
            if set(levarSplit).issubset(set(encontradosSplit)):
                print(f'Que ótimo, consegui encontrar cada um dos {numLevar} itens!')
                print('Isso é tudo! Hora de me preparar!')
                iguais = True
