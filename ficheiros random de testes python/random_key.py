
import random
import string # <----- library string return caracters, numbers and text caracters;

def gerar_senha(tamanho=12): # <------ size key
    caracteres = string.ascii_letters + string.digits + string.punctuation # <--- chama as letras do alfabeto + digitos de 0 a 9 + caracters de pontuação
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) # <-- junta de forma alternada os varios caracteres e letras chamadas até ter o tamanho;
    return senha #<---- retorna o valor gerado

tamanho_senha = 16
nova_senha = gerar_senha(tamanho_senha) #<---- passa o valor da função para a variavel;
print(f"Nova senha gerada:\n\n{nova_senha}\n")