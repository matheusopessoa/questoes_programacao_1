def isPrimo(num):
    lista_Divisores = []
    for i in range(2, num//2 + 1):
        if num % i == 0:
            lista_Divisores.append(num)
    if len(lista_Divisores) == 0:
        print('PRIMO')
    else:
        print('NÃO PRIMO')
def isPerfect(num):
    lista_Divisores = [0]
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            lista_Divisores[0] += i
    if sum(lista_Divisores) == num:
        print('É PERFEITO')
    else:
        print('NÃO É PERFEITO')
num = int(input())
isPrimo(num)
isPerfect(num)
