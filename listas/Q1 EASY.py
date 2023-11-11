lista = []
itensLista, loop = int(input()), 0

while loop != itensLista:
    item = input('')
    if item not in lista:
        lista.append(item)
        loop += 1
    else:
        print('Criatura repetida')
        loop += 1

if loop == itensLista:
    print('Registradas:')
    for x in lista:
        print(x)
