from operacoes import Operacoes

class Teste:

    def __init__(self):
        self.calculadora = Operacoes()

    def soma1(self):
        if self.calculadora.soma(25, 16) == 41:
            print("Caso de teste 1 aprovado")
        else:
            print("Caso de teste 1 reprovado")

    def soma2(self):
        if self.calculadora.soma("Oi", "~") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 2 aprovado")
        else:
            print("Caso de teste 2 reprovado")

    def subtracao1(self):
        if self.calculadora.subtracao(12, 30) == -18:
            print("Caso de teste 3 aprovado")
        else:
            print("Caso de teste 3 reprovado")

    def subtracao2(self):
        if self.calculadora.subtracao(100, "()") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 4 aprovado")
        else:
            print("Caso de teste 4 reprovado")