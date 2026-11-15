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