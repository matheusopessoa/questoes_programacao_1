def contador(entrada):
    contadorMai = 0
    contadorMin = 0
    iguais = False
    for i in entrada:
        if i.isupper():
            contadorMai += 1
        else:
            contadorMin += 1
    if contadorMin == contadorMai:
        iguais = True
    return iguais, contadorMai, contadorMin

palavra = input()
minmax = contador(palavra)
numeroMinusculas, numeroMaiusculas, condicaoIgualdade, tamanhoString = minmax[2], minmax[1], minmax[0], len(palavra)

def numFat(min, mai, iguais, tamanho):
    numeroFatorial = 0
    if iguais == False:
        if min > mai:
            numeroFatorial += min
        else:
            numeroFatorial += mai
    else:
        numeroFatorial += tamanho**2
    return numeroFatorial

numeroFatorial = numFat(numeroMinusculas, numeroMaiusculas, condicaoIgualdade, tamanhoString)

def resultFatorial(numFat): #numFat = numeroFatorial
    if numFat == 0:
        return 1
    else:
        return numFat * resultFatorial(numFat-1)

if condicaoIgualdade == False:
    preco = (resultFatorial(numeroFatorial)) * tamanhoString
else:
    preco = numeroFatorial

if preco >= 100:
    print(f'Hum... {preco}? Acho que na volta eu compro')
else:
    print(f'{preco}! Vou comprar todos!')