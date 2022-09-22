# Devido a COVID-19 os cientistas querem identificar a mais longa sequência comum entre dois trechos de código genético. Para ajudar os cientistas faça um programa que mostre a sequência mais longa comum.

# Entrada:

# Dois trechos de código genético, uma em cada linha

# Saída:

# A mais longa sequência comum entre os trechos de código  




# Por exemplo, dada as sequências

# CAGGGTAGTC

# TCATATC

# a mais longa sequência comum é CATATC.

# Input	Result
# CAGGGTAGTC
# TCATATC
# CATATC

# CAGGGTAGTC
# TCATATC
# 6
# 6
# CCGCAGTGGA
# ACCATGTGAG
# 7
# 4
# CCGCAGTGGAA
# CGTTTGGCGGTCCAGATTGC
# 8
# 8
# CCGCAGTGGAACC
# AACACACCG
# 5
# 4


def sequenciaMaisLonga(sequencia1, sequencia2):
    sequenciasVistas = set()
    sequencias = []
    sequenciaMaisLonga = ''
    maiorExpressao = sequencia1
    menorExpressao = sequencia2
    tamanhoSequencia1 = len(sequencia1)
    tamanhoSequencia2 = len(sequencia2)
    if (tamanhoSequencia2 >= tamanhoSequencia1):
        maiorExpressao = sequencia2
        menorExpressao = sequencia1
    tamanhoMenorExpressao = len(menorExpressao)
    for i in range(1,tamanhoMenorExpressao):
        tamanhoJanela = i+1
        ultimoIndice = i+tamanhoJanela
        if (ultimoIndice > tamanhoMenorExpressao):
            ultimoIndice = tamanhoMenorExpressao 
        for j in range(tamanhoMenorExpressao):
            caracteresJanela = menorExpressao[j:j+tamanhoJanela]
            if len(caracteresJanela) >= tamanhoJanela :
                # sequenciasVistas.add(caracteresJanela)
                sequencias.append(caracteresJanela)
            # print(caracteresJanela)
    for i in range(2,tamanhoMenorExpressao):
        sequenciaLongaDoConjunto = ''
        colecaoRange = filter(lambda caracter: len(caracter) == i, sequencias)
        ultimaPosicao = 0
        for item in colecaoRange:
            posicao = maiorExpressao.find(item)
            if (posicao >= 0):
                if (posicao >= ultimaPosicao):
                    sequenciaLongaDoConjunto += item
                else:
                    sequenciaLongaDoConjunto = item
                ultimaPosicao = posicao

        if (len(sequenciaLongaDoConjunto) > len(sequenciaMaisLonga)):
            sequenciaMaisLonga = sequenciaLongaDoConjunto
    print(len(sequenciaMaisLonga))

arg1=input()
arg2=input()
sequenciaMaisLonga(arg1, arg2)
