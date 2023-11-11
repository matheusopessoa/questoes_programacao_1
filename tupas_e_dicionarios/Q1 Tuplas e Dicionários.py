artistas = {}
nomes_famosos = []
qtd_famosos = int(input())

for i in range(qtd_famosos):
    famoso_atual = input()
    famoso_nome = famoso_atual.split(' - ')[0]
    profissao_mes = famoso_atual.split(' - ')[1]
    profissao, nat_or_fake, mes = profissao_mes.split(' ')[0], profissao_mes.split(' ')[1], profissao_mes.split(' ')[2]
    artista = {
        "nome": famoso_nome,
        "profissao": profissao,
        "nat_or_fake": nat_or_fake,
        "mes": mes
    }
    nomes_famosos.append(famoso_nome)
    repetiu = False
    if len(artistas) > 0:
        if famoso_nome in nomes_famosos:
            indice = nomes_famosos.index(famoso_nome)
            artistas[f'famoso_{indice}'] = artista
            repetiu = True
    if repetiu == False:
        artistas[f'famoso_{i}'] = artista

mes_teste = str(input())
fake_natties = []
for chave, artista in artistas.items():
    mes = artista['mes']
    nat_or_fake_natty = artista['nat_or_fake']
    if mes == mes_teste and nat_or_fake_natty == 'fake':
        fake_natties.append(f'{artista["nome"]} - {artista["profissao"]}')

fake_natties = (sorted(fake_natties))

if len(fake_natties) == 0:
    print('Até agora não temos ninguém pra expor na internet neste mês :(')
else:
    print('Os fake nattys do mês são:')
    for i in fake_natties:
        print(i)

