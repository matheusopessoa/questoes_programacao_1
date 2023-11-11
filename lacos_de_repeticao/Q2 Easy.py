garrafas = 20
pedido_voluntarios = 0
condicao_booleana = True

while condicao_booleana == True:

        if condicao_booleana == True:
            frase = input('')

        if frase == 'Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores':
            jogadores = int(input())
            if jogadores <= garrafas:
                garrafas = garrafas - jogadores

            elif jogadores > garrafas:
                print(f'Não teremos água para todos os jogadores... Temos que garantir {jogadores-garrafas} garrafas!!')
                garrafas = (garrafas*2) - jogadores
                if garrafas < 0:
                    print(f'Estamos devendo {abs(garrafas)} garrafas para os alunos...')
                    condicao_booleana = False

        if frase == 'Encham o cooler, vai começar um jogo!!!!':
            garrafas += 15
            print('Geladeira cheia!')


        if frase == 'Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário':
            pedido_voluntarios -= pedido_voluntarios
            pedido_voluntarios += int(input())
            pedido_voluntarios += int(input())
            pedido_voluntarios += int(input())
            pedido_voluntarios += int(input())
            pedido_voluntarios += int(input())
            if pedido_voluntarios <= garrafas:
                garrafas -= pedido_voluntarios
            elif pedido_voluntarios > garrafas:
                print(f'Prometemos distribuir {abs(garrafas-pedido_voluntarios)} garrafas e zeramos')
                garrafas -= pedido_voluntarios

        if frase == 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas':
            if garrafas > 0:
                print(f'Notícia boa: sobraram {garrafas} garrafas, vamos guardar na geladeira :D')
                condicao_booleana = False
            elif garrafas == 0:
                print('Vendemos todas as águas, fizemos uma contagem certeira!!')
                condicao_booleana = False
            elif garrafas < 0:
                print(f'Estamos devendo {abs(garrafas)} garrafas para os alunos...')
                condicao_booleana = False

        if garrafas > 0 and condicao_booleana == True:
            print(f'Notícia boa: sobraram {garrafas} garrafas, vamos guardar na geladeira :D')
            condicao_booleana = False








