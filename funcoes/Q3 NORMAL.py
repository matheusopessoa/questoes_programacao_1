def distancia(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
def sobreviventes(capsulas, posicaoExplosao, posicaoRaio):
    sobreviventesContador = 0
    centro = []
    for capsule in capsulas:
        sobreviventes = []
        for astronauta in capsule:
            dist = distancia(astronauta[0], astronauta[1], posicaoExplosao[0], posicaoExplosao[1])
            if dist > posicaoRaio:
                sobreviventes.append(astronauta)
        if sobreviventes:
            sobreviventesContador += len(sobreviventes)
            centroid_x = sum(a[0] for a in sobreviventes) / len(sobreviventes)
            centroid_y = sum(a[1] for a in sobreviventes) / len(sobreviventes)
            centro.append([centroid_x, centroid_y])
    return sobreviventesContador, centro
capsulas = eval(input())
posicaoExplosao = eval(input())
posicaoRaio = float(input())
print(list(sobreviventes(capsulas, posicaoExplosao, posicaoRaio)))

