#variaveis
num1 = float (input("Digite o primeiro numero: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float (input("Digite o segundo numero: "))
 
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida"
print(num1, operacao, num2, "=", resultado)


