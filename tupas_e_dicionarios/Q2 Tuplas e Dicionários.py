qtd_famosos = int(input())
natty, fake_natty = [], []

for i in range(qtd_famosos):
    entrada = input().split(' - ')
    nome, nivel, avaliacao = entrada[0], entrada[1], entrada[2]
    artista = (nome, nivel, avaliacao)
    if avaliacao == 'FAKE NATTY':
        fake_natty.append(artista)
    else:
        natty.append(artista)

natty_sorted = sorted(natty, key=lambda x: int(x[1]), reverse=True)
fake_natty_sorted = sorted(fake_natty, key=lambda x: int(x[1]), reverse=True)

for artista in natty_sorted:
    print(f'{artista[0]} - {artista[1]} - natty')
for artista in fake_natty_sorted:
    print(f'{artista[0]} - {artista[1]} - FAKE NATTY')
