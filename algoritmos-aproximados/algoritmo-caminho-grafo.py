from sre_constants import IN


INF = 2
DIST_NULA = '0'
COLUNAS_PERMUTACAO = [1,2,3]
matriz = [[DIST_NULA, 5, 3, 1], 
    [5, DIST_NULA, 10, 4],
    [3, 10, DIST_NULA, 2],
    [1, 4, 2, DIST_NULA]]


for i in COLUNAS_PERMUTACAO:
    for j in COLUNAS_PERMUTACAO:
        for k in COLUNAS_PERMUTACAO:
            if (i!= j and j != k and i != k):
                custo = matriz[0][i] + matriz[i][j] + matriz[j][k] + matriz[k][0]
                print('Custo do caminho ','0', i, j, k, '0', ': ', custo)

