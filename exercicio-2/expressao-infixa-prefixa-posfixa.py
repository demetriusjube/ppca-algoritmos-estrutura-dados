# Faça um algoritmo que calcule o valor de expressões pós-fixas
# Entrada:

# Uma expressão pós fixa com números inteiros de 0 a 9 e as operações de adição e multiplicação, separados por espaços em branco 

# Saída:

# número inteiro com o resultado da expressão

# Exemplo:
# Entrada

# Saída

#  2 5 +

#  7

#  1 2 + 3 4 + *

#  21

# For example:

# Input	Result
# 1 2 + 3 4 + *
# 21


def calculaPosFixa(expressao):
    acumulador = []
    for caracter in expressao.split():
        if (caracter.isnumeric()):
            acumulador.append(int(caracter))
        elif (caracter == '+'):
            soma = acumulador.pop() + acumulador.pop()
            acumulador.append(soma)
        elif (caracter == '*'):
            multiplicacao = acumulador.pop() * acumulador.pop()
            acumulador.append(multiplicacao)
    return acumulador.pop()


x = input()
print(calculaPosFixa(x))