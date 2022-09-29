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


def sequenciaMaisLonga(sequencia1:str, sequencia2:str):
    sequenciaMaisLonga = ''
    maiorExpressao = sequencia1
    menorExpressao = sequencia2
    tamanhoSequencia1 = len(sequencia1)
    tamanhoSequencia2 = len(sequencia2)
    if (tamanhoSequencia2 >= tamanhoSequencia1):
        maiorExpressao = sequencia2
        menorExpressao = sequencia1
    matriz_logica = []
    linha_zeros = []
    for i in range(len(maiorExpressao)):
        linha_zeros.append(0)
    linha_comparacao = [char for char in maiorExpressao]
    coluna_comparacao = [char for char in menorExpressao]
    for i in range(len(menorExpressao)):
        matriz_logica.append(linha_zeros.copy())
    posicao_coluna = 0
    for caracter_coluna in coluna_comparacao:
        posicao_linha = 0
        for caracter_linha in linha_comparacao:
            if (caracter_coluna == caracter_linha):
                matriz_logica[posicao_coluna][posicao_linha] = 1
            posicao_linha += 1
        posicao_coluna += 1
    resultado = linha_zeros.copy()
    for linha in matriz_logica:
        for indice in range(len(linha)):
            resultado[indice]+=linha[indice]
    maiorSeq = ""
    i, j = 0, 0
    while ((i < len(linha_comparacao)) and (j < len(coluna_comparacao))):
        if linha_comparacao[j] == coluna_comparacao[i]:
            maiorSeq = maiorSeq + linha_comparacao[j]
            i, j = i + 1, j + 1
        elif matriz_logica[i + 1][j] >= matriz_logica[i][j + 1]:
            i += 1
        else:
            j += 1
    print(maiorSeq)
    # for indice_marcador in range(len(resultado)):
    #     if (resultado[indice_marcador] > 0):
    #         sequenciaMaisLonga += linha_comparacao[indice_marcador]
    
    # print(sequenciaMaisLonga)

# arg1=input()
# arg2=input()
# sequenciaMaisLonga('CAGGGTAGTC', 'TCATATC')
sequenciaMaisLonga('ACCATGTGAG', 'CCGCAGTGGA')
# sequenciaMaisLonga('CCGCAGTGGAA','CGTTTGGCGGTCCAGATTGC')
# sequenciaMaisLonga('CCGCAGTGGAACC','AACACACCG')

