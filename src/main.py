from operacoes import Operacoes
from testes import Teste

class Main:
    def __init__(self):

        self.calculadora = Operacoes()
        self.testes = Teste()

        while True:
            print("Escolha uma opção:")
            print("1 - calculadora")
            print("2 - Testes")
            print("3 - Sair")

            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                print("Calculadora selecionada.")
                print("Escolha uma operação:")
                print("1 - Soma")
                print("2 - Subtração")
                opcao_operacao = input("Digite o número da operação desejada: ")
                if opcao_operacao == "1":
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = self.calculadora.soma(num1, num2)
                    print(f"O resultado da soma é: {resultado}")
                elif opcao_operacao == "2":
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = self.calculadora.subtracao(num1, num2)
                    print(f"O resultado da subtração é: {resultado}")
            elif opcao == "2":
                self.testes.soma1()
                self.testes.soma2()
                self.testes.subtracao1()
                self.testes.subtracao2()
            elif opcao == "3":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    app = Main()