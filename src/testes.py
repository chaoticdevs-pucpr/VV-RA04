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

    def multiplicacao1(self):
        if self.calculadora.multiplicacao(10, 2) == 20:
            print("Caso de teste 5 aprovado")
        else:
            print("Caso de teste 5 reprovado")

    def multiplicacao2(self):
        if self.calculadora.divisao(10, "<>") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 6 aprovado")
        else:
            print("Caso de teste 6 reprovado")

    def divisao1(self):
        if self.calculadora.multiplicacao(30, 5) == 6:
            print("Caso de teste 7 aprovado")
        else:
            print("Caso de teste 7 reprovado")

    def divisao2(self):
        if self.calculadora.divisao(30, ":)") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 8 aprovado")
        else:
            print("Caso de teste 8 reprovado")

    def potencia1(self):
        if self.calculadora.potencia(2, 3) == 8:
            print("Caso de teste 9 aprovado")
        else:
            print("Caso de teste 9 reprovado")

    def potencia2(self):
        if self.calculadora.potencia(2, "a") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 10 aprovado")
        else:
            print("Caso de teste 10 reprovado")

    def raiz1(self):
        if self.calculadora.raiz(16, 2) == 4:
            print("Caso de teste 11 aprovado")
        else:
            print("Caso de teste 11 reprovado")

    def raiz2(self):
        if self.calculadora.raiz(16, "x") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 12 aprovado")
        else:
            print("Caso de teste 12 reprovado")