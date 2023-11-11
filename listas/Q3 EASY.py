tamanhoMatriz = int(input())
matriz = [[0] * tamanhoMatriz for _ in range(tamanhoMatriz)]
for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):
        matriz[i][j] = int(input())
for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):
        if j != tamanhoMatriz - 1:
            print(matriz[i][j], end=" ")
        if j == tamanhoMatriz - 1:
            print(matriz[i][j], end="")
    print()
