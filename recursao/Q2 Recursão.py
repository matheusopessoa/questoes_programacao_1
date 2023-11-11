def checker(suspeito, stringTeste):
    while len(stringTeste) >= len(suspeito):
        if stringTeste[0:len(suspeito)].lower() == suspeito.lower():
            return stringTeste[0:len(suspeito)]
        else:
            return checker(suspeito, stringTeste[1:])
    return False
suspeito, string_Teste = input(), input()
print(f'Não era o {suspeito}, tenho que continuar procurando.') if checker(suspeito, string_Teste) == False else print(f'Encontrei, o culpado é o {suspeito}!')