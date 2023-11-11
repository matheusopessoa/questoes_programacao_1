#Algoritmo de ordenação crescente (menor pra maior)

def menor(array):
    menorAtual = array[0]
    indiceMenor = 0
    for i in range(1, len(array)):
        if array[i] < menorAtual:
            menorAtual = array[i]
            indiceMenor = i
    return indiceMenor

def ordenacaCrescente(array):
    arrayOrdenada = []
    for i in range(len(array)):
        indiceMenor = menor(array)
        menorNum = array.pop(indiceMenor)
        arrayOrdenada.append(menorNum)
    return arrayOrdenada

arrayTeste = [67, 35, 56, 90, 17, 81, 53, 94, 45, 73, 29, 40, 13, 85, 8, 77, 91, 41, 55, 95, 47, 63, 33, 28, 6, 65, 78, 50, 18, 75, 32, 60, 38, 16, 37, 80, 74, 93, 26, 86, 59, 11, 9, 19, 79, 69, 27, 25, 89, 14, 92, 64, 4, 46, 43, 30, 36, 2, 84, 97, 76, 57, 88, 3, 58, 39, 15, 5, 61, 83, 62, 12, 99, 22, 87, 72, 98, 71, 68, 96, 42, 66, 21, 7, 48, 49, 20, 82, 24, 52, 44, 70, 51, 31, 23, 1, 34, 54, 10, 100, 97]

print(f'O índice do menor número é: {menor(arrayTeste)}\n\nO menor número é {arrayTeste[menor(arrayTeste)]}')
print(f'\nE finalmente, a lista ordenda é:\n{ordenacaCrescente(arrayTeste)}')