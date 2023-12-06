class Calculadora:
    def __init__(self):
        pass
    def adicao(self, num1, num2):
        return num1 + num2
    def subtracao(self, num1, num2):
        return num1 - num2
    def multiplicacao(self,num1, num2):
        return num1 * num2
    def divisao(self, num1, num2):
        if num1 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
# Exemplo de uso
calc = Calculadora()

# Operações
soma = calc.adicao(5, 3)
subtracao = calc.subtracao(10, 4)
multiplicacao = calc.multiplicacao(2, 6)
divisao = calc.divisao(8, 2)

# Exibindo resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

