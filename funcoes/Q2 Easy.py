def inverso(nome):
    return nome[::-1]
def check_Palindromo(nome):
    nome = nome.replace(' ', '').lower()
    nome_Inverso = nome[::-1]
    if nome == nome_Inverso:
        return True
    else:
        return False
def numCaracteresUnicos(frase):
    frase_modificada = frase.replace(' ', '').lower()
    caracteres_distintos = []
    for i in frase_modificada:
        if i not in caracteres_distintos:
            caracteres_distintos.append(i)
    return len(caracteres_distintos)
numFrases = int(input())
for _ in range(numFrases):
    frase = input()
    if check_Palindromo(frase):
        if frase.isdigit():
            print(f'O número "{frase}" é um palíndromo!')
            print(f'Há {numCaracteresUnicos(frase)} número(s) distinto(s) na sequência de números.')
        else:
            print(f'A frase "{frase}" é um palíndromo!')
            print(f'Há {numCaracteresUnicos(frase)} letra(s) distinta(s) na frase.')
    else:
        print('A frase ou o número não é um palíndromo.')
