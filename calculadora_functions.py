#functions
def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ZeroDivisionError("Não é possível fazer a divisão por 0")

def media(num1, num2):
    return (num1 + num2) / 2

def maior_val(num1, num2):
   # return max(num1, num2)
    if num1 > num2:
      return num1
    else:
      return num2


def menor_val(num1, num2):
    # return min(num1, num2)
    if num1 < num2:
      return num1
    else:
      return num2

def dif_absoluta(num1, num2):
    if num1 >= num2:
        return num1 - num2
    else:
        return num2 - num1

#programa
print("Bem-vindo à Calculadora")
print("Selecione a operação a executar, digite '+' para somar, '-' para subtrair, '*' para multiplicar, '/' para dividir")

operacao = input("Introduza a opçao para a operação a executar: ")

try:
    num1 = float(input("Introduza o primeiro valor: "))
    num2 = float(input("Introduza o segundo valor: "))
#se
    if operacao == "+":
        resultado = soma(num1, num2)
        print(f"O resultado da soma de {num1} + {num2} é: {resultado}")
#senão se
    elif operacao == "-":
        resultado = sub(num1, num2)
        print(f"O resultado da subtração de {num1} - {num2} é: {resultado}")
 #senão se
    elif operacao == "*":
        resultado = mult(num1, num2)
        print(f"O resultado da multiplicação de {num1} * {num2} é: {resultado}")
#senão
    elif operacao == "/":
        resultado = div(num1, num2)
        print(f"O resultado da divisão de {num1} / {num2} é: {resultado}")

# calculos finais
    print(f"A média de {num1} e {num2} é: {round(media(num1, num2),2)}")
    print(f"O maior valor entre {num1} e {num2} é: {maior_val(num1, num2)}")
    print(f"O menor valor entre {num1} e {num2} é: {menor_val(num1, num2)}")
    print(f"A diferença absoluta entre {num1} e {num2} é: {round(dif_absoluta(num1, num2),2)}")

except ValueError:
    print("Por favor, confirme que introduziu valores numéricos reais.")
except ZeroDivisionError as errozero:
    print(errozero)