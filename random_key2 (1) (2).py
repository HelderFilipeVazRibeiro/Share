
import random
import string # <----- library string return caracters, numbers and text caracters;


def gerar_senha(palavrachave,key): # <------ size key
    caracteres = string.ascii_letters + string.digits + string.punctuation # <--- chama as letras do alfabeto + digitos de 0 a 9 + caracters de pontuação
    senha = ""
    
    for i in palavrachave:
        #key=>avança x(key) casas no abecedário e adiciona caracteres aleatórios
        novo_index=string.ascii_letters.index(i)+key
        senha+= string.ascii_letters[novo_index] + random.choice(caracteres) 
    
    
    return senha #<---- retorna o valor gerado


nova_senha = gerar_senha("Ola",2) #<---- passa o valor da função para a variavel;
print(f"Nova senha gerada:\n\n{nova_senha}\n")