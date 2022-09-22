# Implementa uma classe Pilha usando listas de Python 3 com os seguintes métodos:

# a) estaVazio() : retorna True ou False

# b) push(item) : coloca item no topo da pilha

# c) pop() : tira e retorna o item no topo da pilha

# d) tamanho() : retorna a quantidade de itens na pilha.

# em seguida implemente a função verificaParanteses(string) que testa se uma string de parenteses está balanceada.

# For example:

# Input	Result
# ()
# True
# (()
# False
# ())
# False

class Pilha:
    
    def __init__(self):
        self.data = []

    def estaVazio(self):
        return self.tamanho() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def tamanho(self):
        return len(self.data)

def verificaParanteses(expressao):
    pilha = Pilha()
    
    for caracter in expressao:
        if caracter == '(':
            pilha.push(caracter)
        elif caracter == ')':
            if pilha.tamanho() > 0:
                pilha.pop()
            else:
                pilha.push(')')
                break
        
    return pilha.estaVazio()

x = input()
print(verificaParanteses(x))