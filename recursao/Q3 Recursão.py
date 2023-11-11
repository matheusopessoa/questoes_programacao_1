numSalas = int(input())
listaSalas = [[] for _ in range(numSalas)]
for i in range(numSalas):
    listaSalas[i] += input().split(' - ')
inicioBusca = int(input())
padrao = ['◇', 'Zelda', 'Agahnim', 'espada']

ruppie, espada, salasIteradas, primeiraBusca = [0], [False], [], [inicioBusca]
def busca(lista, sala):
    chave = 0
    princesa, enemy = False, False
    for i in lista[sala]:
        if sala not in salasIteradas:
            if i not in padrao:
                chave += int(i)
            elif i == '◇':
                ruppie[0] += 1
            elif i == 'Zelda':
                princesa = True
            elif i == 'Agahnim':
                enemy = True
            elif i == 'espada':
                espada[0] = True
        else:
            return f'Infelizmente a princesa ainda corre perigo, mas temos {ruppie[0]} rupees para nos ajudar nas buscas'
    if sala == inicioBusca and len(salasIteradas) != 0:
        return f'Infelizmente a princesa ainda corre perigo, mas temos {ruppie[0]} rupees para nos ajudar nas buscas'
    else:
        salasIteradas.append(sala)
    if len(salasIteradas) == numSalas and enemy == enemy == False:
        return f'Infelizmente a princesa ainda corre perigo, mas temos {ruppie[0]} rupees para nos ajudar nas buscas'
    if espada[0] == True and enemy == True:
        return f'A princesa Zelda está a salvo e ainda conseguimos coletar {ruppie[0]} rupees'
    elif princesa == True:
        if enemy == False:
            return f'A princesa Zelda está a salvo e ainda conseguimos coletar {ruppie[0]} rupees'
        elif enemy == True and espada[0] == False:
            return f'Infelizmente a princesa ainda corre perigo, mas temos {ruppie[0]} rupees para nos ajudar nas buscas'
        elif enemy == True and espada[0] == True:
            return f'A princesa Zelda está a salvo e ainda conseguimos coletar {ruppie[0]} rupees'
    elif enemy == True and espada[0] == False:
        return f'Infelizmente a princesa ainda corre perigo, mas temos {ruppie[0]} rupees para nos ajudar nas buscas'
    else:
        return busca(lista, chave)

print(busca(listaSalas, inicioBusca))




