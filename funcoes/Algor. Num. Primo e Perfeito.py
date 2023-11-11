def isPrimo(num):
    lista_Divisores = []
    for i in range(2, num//2 + 1):
        if num % i == 0:
            lista_Divisores.append(num)
    if len(lista_Divisores) == 0:
        return 'É primo!'
    else:
        return 'Não é primo'
def isPerfect(num):
    lista_Divisores = [0]
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            lista_Divisores[0] += i
    if sum(lista_Divisores) == num:
        return 'é perfeito!'
    else:
        return 'não é perfeito'

num = int(input())
curiosidade = 'Curiosidade: nenhum número é Primo e Perfeito simultaneamente'
print(f'{isPrimo(num)} e {isPerfect(num)}.\n{curiosidade}')
