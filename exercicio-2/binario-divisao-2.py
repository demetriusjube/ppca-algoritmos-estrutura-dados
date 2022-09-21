# Usando a classe Pilha com os métodos empilha(item), desempilha(), tamanho() e estaVazio() implemente a funcao decimal2binario(numero) que  converta números decimais em binário retornando o número binário como uma string de "0"s e "1"s .

# For example:

# Test	Result
# print(decimal2binario(10))
# 1010

def decimal2binario(numero):
    #Para realizar a conversão de decimal para binário, realiza-se a divisão sucessiva por 2 (base do sistema binário). O resultado da conversão será dado pelo último quociente (MSB) e o agrupamento dos restos de divisão será o número binário.
    stack = []
    base = 2
    if (numero <= 0):
        return '0'
    elif (numero == 1):
        return '1'
    elif (numero >= base):
        while (numero >= base):
            quociente = int(numero/base)
            resto = numero%base
            stack.append(str(resto))
            numero = quociente
        stack.append(str(numero))
        binario = ''
        quantidadeEntradas = len(stack)
        for i in range(quantidadeEntradas):
            binario += stack.pop()
        return binario
    return ''


print(decimal2binario(2))
