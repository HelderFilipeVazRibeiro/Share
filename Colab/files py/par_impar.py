def parimpar():
  try:
    print("Colque um número inteiro para saber se é par ou impar:")
    num = int(input("Digite um número para saber se é par ou impar: "))

    if par_impar(num):
       print( f"Escolheu o número {num}, este número é PAR!")
    else:
       print( f"Escolheu o número {num}, este número é IMPAR!")

  except ValueError:
    print("Por favor, certifique-se de que introduziu os valores corretos.")

def par_impar(n):
      return n % 2 == 0


parimpar()
