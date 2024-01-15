
def media(numeros):
    return sum(numeros) / len(numeros)

def numero_maior(numeros):
    return max(numeros)

def numero_menor(numeros):
    return min(numeros)

def dif_absoluta(numeros):
    return abs(max(numeros) - min(numeros))

def soma(numeros):
    return sum(numeros)

#list
numeros = []

while True:
    print("Selecione um das opções: ")
    print("1. Adicionar um número à lista")
    print("2. Consultar os números da list")
    print("3. Remover um número da lista")
    print("4. Operações com valores da lista")
    print("5. Terminar Programa")

    opcao = input("Selecione a opção pretendida: ")

    if opcao == "1":
        novo_numero = input("Introduza um número à lista: ")
        try:
            novo_numero = float(novo_numero)
            numeros.append(novo_numero)
            print(f"O número '{novo_numero}' foi adicionado à lista.\n")
        except ValueError:
                print("Por favor, introduza um número válido.")
            
    elif opcao == "2":
        if not numeros:
            print("A lista está vazia.\n")
        else:
            print("A lista contém os seguintes números:")
            for i, novo_numero in enumerate(numeros, start=1):
                print(f"{i} - {novo_numero}")

    elif opcao == "3":
        if not numeros:
            print("A lista está vazia.\n")
        else:
            try:
                indice = int(input("Introduza o id do número que deseja remover da lista\n"))

                if 1 <= indice <= len(numeros):
                    remover_numero = numeros.pop(indice - 1)
                    print(f"O número '{remover_numero}' foi removido da lista com sucesso!\n")
                    
                else:
                    print("Por favor, certifique-se de que introduziu um valor correto!\n")

            except ValueError:
                print("Por favor, certifique-se de que introduziu um valor correto!\n")
                
    elif opcao == "4":
        if not numeros:
            print("A lista está vazia, não é possível realizar operações.\n")
        else:
            print("Selecione a operação a executar, digite:")
            print("1. Calcular a média da lista")
            print("2. Encontrar o maior número da lista")
            print("3. Encontrar o menor número da lista")
            print("4. Calcular a diferença absoluta entre o maior e o menor numero")
            print("5. Calcula a soma de todos os numeros")
            
            operacao = input("Introduza o número da operação desejada: ")

            if operacao == "1":
                media = media(numeros)
                print(f"A média da lista de numeros é: {round(media, 2)}")

            elif operacao == "2":
                maior = numero_maior(numeros)
                print(f"O maior valor da lista de numeros é: {maior}\n")

            elif operacao == "3":
                menor = numero_menor(numeros)
                print(f"O menor valor da lista de numeros é: {menor}\n")

            elif operacao == "4":
                diferenca = dif_absoluta(numeros)
                print(f"A diferença absoluta entre o maior e o menor valor é: {round(diferenca, 2)}.\n")

            elif operacao == "5":
                soma = soma(numeros)
                print(f"A soma de todos os números da lista é: {soma}\n")
            
            else:
                print("Operação inválida.\n")

    elif opcao == "5":
        print("Programa terminado! Volte sempre!\n")
        break
    
    else:
        print("Por favor, certifique-se de que a opção introduzida é valida!\n")