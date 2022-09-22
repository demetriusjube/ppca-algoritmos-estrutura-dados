# A sequência de Fibonacci é definida mediante a seguinte fórmula:

# F(n+2) = F(n+1) + F(n), para n>=1 e F(1)=F(2)=1.

# Faça um programa que calcule o n-ésimo termo de sequência de Fibonacci, otimizando o uso da memória do computador, de tal forma que ele sirva para calcular termos para n grandes.

# For example:

# Input	Result
# 10
# 55


def fibonacciList(valor):
    if (valor <= 2):
        return 1
    else:
        lista = [0,1]
        for i in range(valor-1):
            f_n=lista[0]
            f_n_1 = lista[1]
            f_n_2 = f_n + f_n_1
            lista.pop(0)
            lista.append(f_n_2)
        return lista[1]

valor = int(input())
print(fibonacciList(valor))