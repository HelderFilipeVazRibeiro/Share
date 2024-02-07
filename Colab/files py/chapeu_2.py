def chapeu():
    try:
        print("Está a chover hoje?\n")
        num = input("Digite sim ou não: ")

        if num.lower() == "sim":
            print("Então não pode sair de casa sem chapéu!")
        else:
            print("Então vai trabalhar!")

        num2 = input("Tem chapéu de chuva para sair de casa?\nDigite sim ou não:\n")

        if num2.lower() == "sim":
            print("Então podes ir trabalhar!")
        else:
            print("Então vai comprar um chapéu de chuva :)")

    except ValueError:
        print("Por favor, certifique-se de que introduziu os valores corretos.")

chapeu()
