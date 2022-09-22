# Implemente a classe Stack em Python 3 com os seguintes métodos:

# isEmpty()

#  push(item)

# pop()

# size()

# e escreva um programa usando a classe Stack para verificar se os símbolos "(", "[", "{", "}", "]" e ")" estão balanceados.form  

# For example:

# Input	Result
# ([{}])
# True
# (]
# False

class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def size(self):
        return len(self.data)

def isSimbolosBalanceados(expressao):
    stack = Stack()
    
    for caracter in expressao:
        if caracter == '(' or caracter == '[' or caracter == '{':
            stack.push(caracter)
        else:
            ultimoElemento = stack.data[-1]
            if (caracter == ")" and ultimoElemento == "(") or (caracter == "]" and ultimoElemento == "[") or (caracter == "}" and ultimoElemento == "{"):
                stack.pop()
            else:
                return False
        
    return stack.isEmpty()

x = input()
print(isSimbolosBalanceados(x))
