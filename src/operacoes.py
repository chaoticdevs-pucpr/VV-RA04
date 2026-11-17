import math

class Operacoes:

    def __init__(self):
        pass

    def soma(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            return num1 + num2
        else:
            return "Erro: a calculadora só aceita números racionais"

    def subtracao(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            return num1 - num2
        else:
            return "Erro: a calculadora só aceita números racionais"

    def multiplicacao(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            return num1 * num2
        else:
            return "Erro: a calculadora só aceita números racionais"

    def divisao(self, num1, num2):
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                return num1 / num2
            else:
                return "Erro: a calculadora só aceita números racionais"

    def potencia(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            return num1 ** num2
        else:
            return "Erro: a calculadora só aceita números racionais"

    def raiz(self, num1, num2=2):
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            return "Erro: a calculadora só aceita números racionais"
        if num2 == 0:
            return "Erro: o índice da raiz não pode ser zero"
        if num1 < 0:
            if num2 % 2 == 0:
                return "Erro: não é possível calcular raiz de índice par de número negativo"
            return -((-num1) ** (1 / num2))
        return num1 ** (1 / num2)

    def logaritmo(self, num1, num2):
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            return "Erro: a calculadora só aceita números racionais"
        if num1 <= 0:
            return "Erro: o logaritmando deve ser maior que zero"
        if num1 <= 0 or num2 <= 0 or num2 == 1:
            return "Erro: logaritmo indefinido para esses valores"
        return math.log(num1, num2)

    def fatorial(self, num1):
        if not isinstance(num1, (int, float)) or isinstance(num1, bool):
            return "Erro: a calculadora só aceita números racionais"
        if num1 < 0:
            return "Erro: não existe fatorial de número negativo"
        return math.factorial(int(num1))