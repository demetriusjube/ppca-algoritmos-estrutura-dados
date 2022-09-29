# Suponha que você é o programador de uma máquina de vendas automáticas. Ela não só tem que dar o troco certo, mas com o menor número de moedas possíveis. 

# Entrada:

# Um valor N inteiro que é a quantidade de valores de moedas existentes no sistema monetário de um país fictício.

# N valores reais correspondentes às moedas do sistema monetário de um país fictício, já ordenadas de forma decrescente, em uma única linha separados por espaços em branco.

# Dois números reais valor da nota de entrada e valor da compra, separados espaço em branco.

# Saída:

# As moedas usadas por linha, começando pela moeda de maior valor.

# For example:

# Input	Result
# 4
# 0.25 0.10 0.05 0.01
# 1.00 0.37
# 0.25
# 0.25
# 0.10
# 0.01
# 0.01
# 0.01

def calcularTroco(valoresMoedas, troco, minMoedas, moedasUsadas):
    for centavos in range(troco + 1):
        contadorMoedas = centavos
        novaMoeda = 1
        for posicao in [c for c in valoresMoedas if c <= centavos]:
            if minMoedas[centavos - posicao] + 1 < contadorMoedas:
                contadorMoedas = minMoedas[centavos - posicao] + 1
                novaMoeda = posicao
        minMoedas[centavos] = contadorMoedas
        moedasUsadas[centavos] = novaMoeda
    return minMoedas[troco]


def imprimirMoedas(moedasUtilizadas, troco):
    moeda = troco
    while moeda > 0:
        moedaCorrente = moedasUtilizadas[moeda]
        print("%.2f" % round(moedaCorrente / 100, 2))
        moeda = moeda - moedaCorrente

def getListaMoedas(inputMoedas:str):
    moedas = []
    moedasString = inputMoedas.split()
    for moeda in moedasString:
        moedas.append(int(round(float(moeda) * 100, 2)))
    return moedas

def getTroco(compra:str):
    nota_compra = compra.split()
    troco = float(nota_compra[0]) - float(nota_compra[1])
    return int(round(troco * 100))


def imprimeMoedasTroco(inputMoedas, inputTroco):
    troco = getTroco(inputTroco)
    moedas = getListaMoedas(inputMoedas)
    moedas_usadas = [0] * 100
    cont_moedas = [0] * 100
    calcularTroco(moedas, troco, cont_moedas, moedas_usadas)
    imprimirMoedas(moedas_usadas, troco)

input()     
inputMoedas = input()
inputTroco = input()
imprimeMoedasTroco(inputMoedas, inputTroco)


