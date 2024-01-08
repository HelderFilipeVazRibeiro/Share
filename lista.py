#functions
def soma(numeros):
    return sum(numeros)

def media(numeros):
    return soma(numeros)/len(numeros)

def maior_num(numeros):
    return max(numeros)

def menor_num(numeros):
    return min(numeros)

def iterar_lista(numeros): #lista os valores da lista
    for num in numeros:
        print(num)

def num_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    return pares

numeros = [23, 34, 187, 286, 466]

print(f"Os números existentes na Array são: {numeros}")
print(f"A soma dos números é: {soma(numeros)}")
print(f"A média dos elementos da lista é: {media(numeros)}")
print(f"O maior número na lista é: {maior_num(numeros)}")
print(f"O menor número na lista é: {menor_num(numeros)}")
print("*****************************************************")
print(f"Iterando pela lista:")
iterar_lista(numeros)
print("*****************************************************")

pares=num_pares(numeros)
print("Números Pares da Array são:")
print(f"Os valores pares da array sao: {pares}")