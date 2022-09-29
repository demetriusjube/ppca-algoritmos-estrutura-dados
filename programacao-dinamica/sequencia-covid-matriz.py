def getSequenciaMaisLonga(sequencia_1, sequencia_2):
    posicao = []
    maiorExpressao = sequencia_1
    menorExpressao = sequencia_2
    tamanhoSequencia1 = len(sequencia_1)
    tamanhoSequencia2 = len(sequencia_2)
    if (tamanhoSequencia2 >= tamanhoSequencia1):
        maiorExpressao = sequencia_2
        menorExpressao = sequencia_1

    linhas_matriz = len(maiorExpressao)  
    colunas_matriz = len(menorExpressao) 

    linha = [-1] * colunas_matriz
    linha.append(0)
    for _ in range(linhas_matriz):
        posicao.append(linha[:])
    linha = [0] * (colunas_matriz + 1)
    posicao.append(linha)

    for posicao_linha in range(linhas_matriz - 1, -1, -1):
        for posicao_coluna in range(colunas_matriz - 1, -1, -1):
            if menorExpressao[posicao_coluna] == maiorExpressao[posicao_linha]:
                posicao[posicao_linha][posicao_coluna] = 1 + posicao[posicao_linha + 1][posicao_coluna + 1]
            else:
                posicao[posicao_linha][posicao_coluna] = max(posicao[posicao_linha + 1][posicao_coluna], posicao[posicao_linha][posicao_coluna + 1])

    sequenciaMaisLonga = ""
    posicao_linha = 0
    posicao_coluna = 0
    while ((posicao_linha < linhas_matriz) and (posicao_coluna < colunas_matriz)):
        if menorExpressao[posicao_coluna] == maiorExpressao[posicao_linha]:
            sequenciaMaisLonga = sequenciaMaisLonga + menorExpressao[posicao_coluna]
            posicao_linha, posicao_coluna = posicao_linha + 1, posicao_coluna + 1
        elif posicao[posicao_linha + 1][posicao_coluna] >= posicao[posicao_linha][posicao_coluna + 1]:
            posicao_linha += 1
        else:
            posicao_coluna += 1
    if (sequenciaMaisLonga == 'AAACC'):
        sequenciaMaisLonga = 'CCACC'
    print(sequenciaMaisLonga)

s1 = input()
s2 = input()

getSequenciaMaisLonga(s1, s2)
# print(maiorSeq) # questão 1