def search(trigrama, dicionario, parametro):
    for chave, valor in dicionario.items():
        if trigrama[0].lower() in valor.lower() and parametro.lower() in valor.lower():
            return chave
    return None

def gerar_trigramas(texto):
    trigramas = {}
    for i in range(len(texto) - 2):
        trigrama = texto[i:i + 3].lower()
        if trigrama in trigramas:
            trigramas[trigrama].append(i)
        else:
            trigramas[trigrama] = [i]
    return trigramas

check = {}

while True:
    entrada = input()
    if entrada != 'END_OF_FILE':
        check[len(check)] = entrada.lower()
    else:
        break

qtd_buscas = int(input())

for i in range(qtd_buscas):
    parametro = input().lower()
    trigramas_parametro = gerar_trigramas(parametro)
    chave = search(list(trigramas_parametro.keys()), check, parametro)
    print(chave if chave is not None else -1)
