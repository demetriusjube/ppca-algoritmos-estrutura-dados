# Um grupo de alunos da disciplina Estrutura de Dados, experts em grafos, resolveu abrir uma startup para armazenamento e distribuição de produtos comprados pela Internet. O objetivo deles é colocar pontos de distribuição em cidades de tal forma que os moradores de qualquer cidade fiquem distantes do ponto de distribuição apenas a uma aresta de distância. Para diminuir os custos eles querem minimizar a quantidade de pontos de distribuição.

# Entrada: Uma lista de adjacências de um grafo não dirigido, com a comprimento em Km de cada aresta. A lista termina quando aparece uma distância negativa.

# Saída: A quantidade de pontos de distribuição em uma linha e na outra as cidades onde estão os mesmos, em ordem alfabética. Se houver mais de uma solução, colocar a solução com a menor ordem lexicográfica das cidades.

# For example:

# Input	Result
# A B 1
# A E 2
# A D 3
# B C 4
# B E 5
# C D 6
# C E 7
# D E 8
# X X -1
# 1
# E
# A B 1
# A F 2
# A E 3
# B C 4
# B F 5
# B I 6
# B G 7
# C D 8
# C F 9
# C I 10
# D E 12
# D F 13
# E F 14
# G I 16
# A A -1
# 2
# B
# D
