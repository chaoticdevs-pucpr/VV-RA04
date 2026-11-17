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
        if self.calculadora.multiplicacao(10, "<>") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 6 aprovado")
        else:
            print("Caso de teste 6 reprovado")

    def divisao1(self):
        if self.calculadora.divisao(30, 5) == 6:
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

    def logaritmo1(self):
        if self.calculadora.logaritmo(8, 2) == 3.0:
            print("Caso de teste 13 aprovado")
        else:
            print("Caso de teste 13 reprovado")

    def logaritmo2(self):
        if self.calculadora.logaritmo(8, "x") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 14 aprovado")
        else:
            print("Caso de teste 14 reprovado")

    def fatorial1(self):
        if self.calculadora.fatorial(5) == 120:
            print("Caso de teste 15 aprovado")
        else:
            print("Caso de teste 15 reprovado")

    def fatorial2(self):
        if self.calculadora.fatorial("a") == "Erro: a calculadora só aceita números racionais":
            print("Caso de teste 16 aprovado")
        else:
            print("Caso de teste 16 reprovado")

    def porcentagem1(self):
            if self.calculadora.porcentagem(20, 150) == 30.0:
                print("Caso de teste 17 aprovado")
            else:
                print("Caso de teste 17 reprovado")

    def porcentagem2(self):
        if self.calculadora.porcentagem("a", 150) == "A calculadora só aceita números racionais":
            print("Caso de teste 18 aprovado")
        else:
            print("Caso de teste 18 reprovado")

    def historico1(self):
        if "25 + 16 = 41" in self.calculadora.historico("25 + 16 = 41"):
            print("Caso de teste 19 aprovado")
        else:
            print("Caso de teste 19 reprovado")

    def historico2(self):
        if self.calculadora.historico(123) == "Operação inválida para o histórico":
            print("Caso de teste 20 aprovado")
        else:
            print("Caso de teste 20 reprovado")