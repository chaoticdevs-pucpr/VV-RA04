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