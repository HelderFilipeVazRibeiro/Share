#exemplo 3
x = 4     
x = "Sally"
x = 4       
print(x)

x = str(3)    # x will be string '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#função
def dobro(x):
    return x*2


numeros=[1,2,3,'ola',4]
print(numeros)
for numeros in numeros:
    print(dobro(numeros))
  
    
nome_do_personagem = 'Antonio'
idade_do_personagem = '33'
print ('O nome do nosso personagem é ' + nome_do_personagem + '\ne tem uma idade de ' + idade_do_personagem + 'anos') #concatenar   ----> juntas as string + texto a juntar +  

texto = "Texto Escrito para Teste"
print (texto.upper())
print(texto)
print (texto.lower())

x = texto.rfind("Te")
print(x)

x = texto.index("Te")
print(x)

print("hello world")

print(5)
print(5+5)
print(int(5/4))
print(5/2)
print(2*2)
print(2^3)
print(2**3)

print (round(3.141592653589793, 2))
x2 = 9999.32432
print(round(x2,2))

texto = "O número é: {}".format(x2)
print(texto)

print("Formation 29/11 ")

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
print("O seu nome é", nome)
print("Você tem", idade, "anos.")
input#
