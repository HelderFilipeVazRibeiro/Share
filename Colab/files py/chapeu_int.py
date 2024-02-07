
#chapéu com solução int 
 
def chapeu():
  try:
    print("Está a chover hoje!\nTem chapéu de chuva para sair de casa?\n")
    num = int(input("Digite 1 para Sim e 0 para Não: "))

    if 1:
       print("Então não pode sair de casa!")
    else:
       print("Então vai trabalhar!")

  except ValueError:
    print("Por favor, certifique-se de que introduziu os valores corretos.")

chapeu()