lista_Classificados = [0]
lista_Desclassificados = [0]
isFim = []
def turnInt(value):
    return int(value)
def apresentacao(nome):
    print(f'--- Participante: {nome} ---')
def ficha_Class(numprop, finalprop, velprop):
    print(f'Qtd de propulsores Final: {finalprop}')
    print(f'Velocidade Inicial: {numprop * velprop} km/h')
    print(f'Velocidade Final: {finalprop * velprop} km/h')
def situations(enter):
    enter = input('')
    if enter != 'FIM':
        enter = enter.split(' ')
        nome = enter[0]
        props = turnInt(enter[1])
        finalProps = 0
        finalProps += turnInt(enter[1])
        velProps = turnInt(enter[2])
        classificado = False
        desclassificado = False
        while not desclassificado and not classificado:
            situation = input()
            if situation == 'FIM':
                classificado = True
                lista_Classificados[0] += 1
                apresentacao(nome)
                ficha_Class(props, finalProps, velProps)
                isFim.append('Supõe tu um campo de batatas e duas tribos famintas. As batatas apenas chegam para alimentar uma das tribos que assim adquire forças para transpor a montanha e e ir à outra vertente, onde há batatas em abundância; mas, se as duas tribos dividirem em paz as batatas do campo, não chegam a nutrir-se suficientemente e morrem de inanição. A paz nesse caso, é a destruição; a guerra é a conservação. Uma das tribos extermina a outra e recolhe os despojos. Daí a alegria da vitória, os hinos, aclamações, recompensas públicas e todos os demais feitos das ações bélicas. Se a guerra não fosse isso, tais demonstrações não chegariam a dar-se, pelo motivo real de que o homem só comemora e ama o que lhe é aprazível ou vantajoso, e pelo motivo racional de que nenhuma pessoa canoniza uma ação que virtualmente a destrói. Ao vencido, ódio ou compaixão; ao vencedor, as batatas')
            elif situation == 'Pit-Stop Espacial':
                finalProps += 1
            elif situation == 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.':
                finalProps -= 1
                if finalProps == 0:
                    lista_Desclassificados[0] += 1
                    print(f'BUUMM!! Infelizmente, {nome} está fora da corrida.')
                    break
            elif situation == 'Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1...':
                lista_Desclassificados[0] += 1
                print(f'O {nome} achou que não descobriríamos, tirem {nome} imediatamente da pista.')
                break
            elif situation == 'Próximo':
                classificado = True
                lista_Classificados[0] += 1
                apresentacao(nome)
                ficha_Class(props, finalProps, velProps)
            if len(isFim) != 0:
                if lista_Classificados[0] >= 1:
                    print(f'Relatório da CIn Pod Race: {lista_Classificados[0]} participantes terminaram a corrida e {lista_Desclassificados[0]} foram desclassificados.')
                else:
                    print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")
    else:
        isFim.append('Supõe tu um campo de batatas e duas tribos famintas. As batatas apenas chegam para alimentar uma das tribos que assim adquire forças para transpor a montanha e e ir à outra vertente, onde há batatas em abundância; mas, se as duas tribos dividirem em paz as batatas do campo, não chegam a nutrir-se suficientemente e morrem de inanição. A paz nesse caso, é a destruição; a guerra é a conservação. Uma das tribos extermina a outra e recolhe os despojos. Daí a alegria da vitória, os hinos, aclamações, recompensas públicas e todos os demais feitos das ações bélicas. Se a guerra não fosse isso, tais demonstrações não chegariam a dar-se, pelo motivo real de que o homem só comemora e ama o que lhe é aprazível ou vantajoso, e pelo motivo racional de que nenhuma pessoa canoniza uma ação que virtualmente a destrói. Ao vencido, ódio ou compaixão; ao vencedor, as batatas')
        if lista_Classificados[0] >= 1:
            print(f'Relatório da CIn Pod Race: {lista_Classificados[0]} participantes terminaram a corrida e {lista_Desclassificados[0]} foram desclassificados.')
        else:
            print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")

while len(isFim) == 0:
    nome = ''
    situations(nome)

