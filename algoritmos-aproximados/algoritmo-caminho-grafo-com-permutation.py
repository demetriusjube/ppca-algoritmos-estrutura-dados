from itertools import permutations
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

permutacoes = permutations([1,2,3], 3)
# for linha in permutacoes:
#     print(linha)

for linha in permutacoes:
    primeiraColuna = linha[0]
    segundaColuna = linha[1]
    terceiraColuna = linha[2]
    custo = matriz[0][primeiraColuna] + matriz[primeiraColuna][segundaColuna] + matriz[segundaColuna][terceiraColuna] + matriz[terceiraColuna][0]
    caminho = '0'+ str(primeiraColuna) + str(segundaColuna) +str(terceiraColuna) +'0'
    if (custo < menor_custo):
        menor_custo = custo
        menor_caminho = caminho
    print('Custo do caminho ',caminho, ': ', custo)

print('Menor ciclo: ', menor_caminho, ' com custo ', menor_custo)

