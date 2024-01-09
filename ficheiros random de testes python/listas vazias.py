numeros = []#cria uma lista no programa que guarda os valores inseridos pelo utilizador;
limite = 20

while len(numeros) < limite:
    try:
        num: float(input("Digite os valores a adicionar à lista: "))
        if num < 0:
            break
        numeros.append(num)
    except ValueError:
        print("Por favor verifique que introduziu um valor correcto")
        
if not numeros:
    print("A lista encontra-se vazia, pff certifique-se que adicionou pelo menos um número")
else:
    soma = sum(numeros)
    media = soma / len(numeros)
    maior_numero = max(numeros)
    menor_numero = min(numeros)

    print(f"O valor da soma dos números da lista é {soma}")
    print(f"O valor médio dos números da lista é {media}")
    print(f"O maior numero da lista é: {maior_numero}")
    print(f"O menor numero da lista é: {menor_numero}")
    
print("Itens listados na lista:")
for numero in numeros:
    print(numero)
    
    numeros_pares = [num for num in numeros if num % 2 == 0]
    if numeros_pares:
        print(f" A lista contém os seguintes números pares: {numeros_pares}")
    else:
        print("A lista não contém números pares")
    
    if len(numeros) == limite:
        print(f"A lista tem um limite de {limite}(espaço na lista), pelo que a lista ficou concluida e os calculos foram feitos")