primeiro = input('')
indicePrimeiro = int(input())
segundo = input('')
indiceSegundo = int(input())
terceiro = input('')
indiceTerceiro = int(input())
quarto = input('')
indiceQuarto = int(input())
quinto = input('')
indiceQuinto = int(input())

ia = (primeiro == 'ativação de inteligência artificial' or segundo == 'ativação de inteligência artificial' or terceiro == 'ativação de inteligência artificial' or quarto == 'ativação de inteligência artificial' or quinto == 'ativação de inteligência artificial')
membranas = (primeiro == 'membranas planadoras' or segundo == 'membranas planadoras' or terceiro == 'membranas planadoras' or quarto == 'membranas planadoras' or quinto == 'membranas planadoras')
lancador = (primeiro == 'novo lançador de teias' or segundo == 'novo lançador de teias' or terceiro == 'novo lançador de teias' or quarto == 'novo lançador de teias' or quinto == 'novo lançador de teias')

energia_total = indicePrimeiro + indiceSegundo + indiceTerceiro + indiceQuarto + indiceQuinto



if (primeiro == 'novo lançador de teias') and ((segundo != 'NADA') or (terceiro != 'NADA') or (quarto != 'NADA') or (quinto != 'NADA')):
     print ('Com calma, aranha')


if primeiro == 'novo lançador de teias' and segundo == 'lentes de visão avançada':
    print('Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro')

if primeiro == 'novo lançador de teias' and segundo == 'lentes de visão avançada' and terceiro == 'traje à prova de balas':
        print('UOU, só tente sair dessa vivo, vou otimizar a energia aqui')

if ia:
    print('Espero que não esteja ativando isso para usar nas provas')

if energia_total >= 80:
    print('Vou descarregar em questão de minutos, pare AGORA')

if ia and membranas and lancador:
    print('Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa')

print(f'Aranha, nessa sequência você usou {energia_total} de energia!')