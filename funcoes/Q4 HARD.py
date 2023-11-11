#Nessa questão, me desafiei a fazer no mínimo de linhas possível, apenas como entretenimento. O que quero dizer com isso
#é que esse não é meu estilo de programação, pois gosto de prezar pelo clean code e facilidade de leitura de código.
def isPerfect(num):
    divisores, meio = [], int(num)//2 + 1
    for i in range(meio):
        i += 1
        if num%i == 0:
            divisores.append(i)
    if sum(divisores) == num and len(divisores) > 1:
        return 1
    else:
        return 0
def postfix_to_infix(postfix_expression):
    stack = []
    for algorism in postfix_expression:
        if algorism.isdigit():
            stack.append(algorism)
        else:
            operand2, operand1 = stack.pop(), stack.pop()
            expression = f"({operand1} {algorism} {operand2})"
            stack.append(expression)
    return stack[0]
endGame, contador, valores, decodificada = False, 0, [], ''
while not endGame:
    entrada = input()
    if entrada == 'Todas as expressoes foram enviadas!':
        endGame = True
    elif entrada == '':
        contador += 1
        binary = ''.join(str(bit) for bit in valores)
        decimal = int(binary, 2)
        asc = chr(decimal)
        decodificada+=asc
        print(f'O {contador}º conjunto de expressoes resultou no binario {binary} que em ASCII eh: {asc}\n')
        valores, binary = [], 0
    else:
        entrada = entrada.split()
        valores.append(isPerfect(int(eval(postfix_to_infix(entrada)))))
print(f"A decodificacao final resultou em:\n{decodificada}")