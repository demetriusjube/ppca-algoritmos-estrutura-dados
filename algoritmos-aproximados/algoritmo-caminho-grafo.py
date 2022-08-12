from sre_constants import IN


INF = 999999
DIST_NULA = '0'
COLUNAS_PERMUTACAO = [1,2,3]
matriz = [[DIST_NULA, 5, 3, 1], 
    [5, DIST_NULA, 9, 4],
    [3, 9, DIST_NULA, 2],
    [1, 4, 2, DIST_NULA]]

menor_custo = INF 
menor_caminho = ''

for i in COLUNAS_PERMUTACAO:
    for j in COLUNAS_PERMUTACAO:
        for k in COLUNAS_PERMUTACAO:
            if (i!= j and j != k and i != k):
                custo = matriz[0][i] + matriz[i][j] + matriz[j][k] + matriz[k][0]
                caminho = '0'+ str(i) + str(j) +str(k) +'0'
                if (custo < menor_custo):
                    menor_custo = custo
                    menor_caminho = caminho
                print('Custo do caminho ',caminho, ': ', custo)

print('Menor ciclo: ', menor_caminho, ' com custo ', menor_custo)