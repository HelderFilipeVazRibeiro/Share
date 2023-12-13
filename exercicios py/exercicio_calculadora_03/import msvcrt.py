import curses

def get_key():          #   definição de uma nova função
    return curses.getch().decode('utf-8')      

#   utilização da função (getch) e (decode) para intrepretar a intrudução do operador na calculadora

##################### INICIO DA CALCULADORA ################################################

calc = Calculadora() # Chamada da classe ao "programa"

while True: # inicio do loop do calculo
    numero1 = float(input("Indique o primeiro número: ")) #  Pedido para a Introdução do primeiro Valor

    while True: # inicio do loop para o operador 
        print("Qual o operador? \",*,-,+\"")
        # Apresentação de uma mensagem para o utilizador a pedir a introdução do operador, que será aceite de imidiato.
        operador = get_key()
        #  Antes tinhamos input() em que o utilizador teria de pressionar a tecla enter, e passamos a definir (def) uma função chamada (get_key) para que a introdução seja aceite automáticamente.

        if operador in ['+', '-', '*', '/']:
            break #se tiver certo breack e continua com o proximo codigo
        else:
            print("Operador inválido. Tente novamente.")

   
    numero2 = float(input("Indique o segundo número: ")) #  Pedido para a Introdução do segundo Valor

    resultado = calc.calcular(numero1, operador, numero2) # Realiza o cálculo dos diferentes valores dependendo do operador introduzido
    print ("Resultado:", resultado) # Apresenta o resultado final da operação.

    print("Pressione 'Esc' para sair ou qualquer tecla para continuar.")
    tecla = get_key()
    
    if tecla == '\x1b':  # Se a tecla pressionada for 'Esc'
        break