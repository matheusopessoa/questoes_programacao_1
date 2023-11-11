medica = ['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta', 'Celular']
assistenteInformatica = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']
padeira = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
economista = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
personalTrainer = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']
sair = False

bolsa = []
itensDia = []

prevista = input('')
real = input('')

if prevista == 'Medica':
    bolsa = medica.copy()
elif prevista == 'Assistente de Informatica':
    bolsa = assistenteInformatica.copy()
elif prevista == 'Padeira':
    bolsa = padeira.copy()
elif prevista == 'Economista':
    bolsa = economista.copy()
elif prevista == 'Personal Trainer':
    bolsa = personalTrainer.copy()

if real == 'Medica':
    itensDia = medica.copy()
elif real == 'Assistente de Informatica':
    itensDia = assistenteInformatica.copy()
elif real == 'Padeira':
    itensDia = padeira.copy()
elif real == 'Economista':
    itensDia = economista.copy()
elif real == 'Personal Trainer':
    itensDia = personalTrainer.copy()

while not sair:
    acao = input()
    if acao == 'Adicionar':
        itemAdicionado = input()
        if itemAdicionado in bolsa:    #já ta na bolsa
            print(f'Barbie, você já colocou {itemAdicionado} na bolsa')
        elif itemAdicionado not in bolsa and itemAdicionado in itensDia:     #certo
            print(f'{itemAdicionado} adicionado à bolsa')
            bolsa.append(itemAdicionado)
        elif itemAdicionado not in bolsa and itemAdicionado not in itensDia:    #profissao errada
            print(f'Barbie, {itemAdicionado} não esta na lista de itens de {real}')
    elif acao == 'Retirar':
        itemRetirado = input()

        if itemRetirado in bolsa and itemRetirado not in itensDia:  #certo
            print(f'{itemRetirado} retirado da bolsa')
            bolsa.remove(bolsa[bolsa.index(itemRetirado)])
        elif itemRetirado in itensDia and itemRetirado in bolsa:  #errrada
            print(f'Não faca isso Barbie, você precisa de {itemRetirado} para trabalhar de {real}')
        elif itemRetirado not in bolsa:   #nao ta na bolsa
            print('Barbie, como você vai retirar algo que já não esta ai?')
    elif acao == 'Sair':
        sair = True

if sair == True:
    bolsa = sorted(bolsa)
    print('Itens na bolsa: ', end='')
    for itemOrdenado in range(0, len(sorted(bolsa))):
        print(bolsa[itemOrdenado], end=', ') if itemOrdenado < (len(bolsa) - 1) else print(bolsa[itemOrdenado])

    if sorted(bolsa) == sorted(itensDia):
        print('Boa Barbie, foi na correria mas tudo deu certo!')
    elif len(bolsa) < len(itensDia):
        print(f'Oh não!! Barbie, você esqueceu de pegar {list(set(itensDia) - set(bolsa))[0]}!!')
    elif len(bolsa) > len(itensDia) and set(bolsa).difference(itensDia) not in itensDia: #tem tudo e algo a mais
        print(f'Barbie, você esqueceu de tirar {list(set(bolsa).difference(itensDia))[0]}, você não usa ele trabalhando de {real}')

