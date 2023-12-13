class Calculadora:
    def __init__(self):
        pass

    def calcular(self, num1, operador, num2):
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                return "Erro: Divisão por zero."
            else:
                return num1 / num2
        else:
            return "Operador inválido."

# FORA DA CLASS

calc = Calculadora() # Chamada da classe ao "programa"

numero1 = int(input("Indique o primeiro número: "))
operador = input()
numero2 = int(input("Indique o segundo número: "))

resultado = calc.calcular(numero1, operador, numero2)
print("Resultado:", resultado)