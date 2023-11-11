caracteristica1 = input('')

if caracteristica1 != 'Humildade':
    print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
    print('Infelizmente você não possui as característica necessárias!')
else:
    caracteristica2 = input('')
    if caracteristica2 != 'Bondade':
        print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
        print('Infelizmente você não possui as característica necessárias!')
    else:
        paixao = input('')
        if paixao != 'Mary' and paixao != 'Ninguem':
            print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
            print('Infelizmente você não está apaixonado pela pessoa certa!')
        else:
            habilidade = input('')
            if habilidade != 'Lancar' and habilidade != 'Dancar':
                print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
                print('Infelizmente você não possui as habilidades necessárias!')
            else:
                nota1 = int(input())
                nota2 = int(input())
                nota3 = int(input())
                somaNotas = nota1 + nota2 + nota3
                mediaNotas = somaNotas / 3
                if mediaNotas >= 7:
                    print("Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!")
                else:
                    print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
                    print('Infelizmente você não obteve um bom desempenho escolar!')



