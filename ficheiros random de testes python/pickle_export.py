import os
import pickle
from IPython.display import clear_output

class DadosAlunos:
    def __init__(self):
        self.nomes = []
        self.numeros = []
        self.moradas = []
        self.bi_cc = []
        self.telefones = []
        self.emails = []

class DadosAlunosMestrado(DadosAlunos):
    def __init__(self):
        super().__init__()
        self.temas_tese = []
        self.alunos_mestrado = []

#Instanciação dos dados dos alunos e dos dados de mestrado
dados_alunos = DadosAlunos()
dados_alunos_mestrado = DadosAlunosMestrado()

indice_aluno = 1  #Índice do próximo aluno a ser adicionado

def atualizar_numeros_alunos():
    global indice_aluno
    indice_aluno = len(dados_alunos.numeros) + 1

def listar_turma():
    if not dados_alunos.nomes:
        print("A turma está vazia.")
    else:
        print("Lista de Alunos:")
        for indice, (nome, numero, morada, bi_cc, telefone, email) in enumerate(zip(dados_alunos.nomes, dados_alunos.numeros, dados_alunos.moradas, dados_alunos.bi_cc, dados_alunos.telefones, dados_alunos.emails), start=1):
            #Imprime a lista de alunos enumerando-os
            print(f"Aluno {indice}: {nome} (Número: {numero}), Morada: {morada}, Bi/CC: {bi_cc}, Telefone: {telefone}, E-Mail: {email}")

        if dados_alunos_mestrado.alunos_mestrado:
            print("\nAlunos de Mestrado:")
            for i, aluno_mestrado in enumerate(dados_alunos_mestrado.alunos_mestrado, start=1):
                print(f"Aluno de Mestrado {i}: {aluno_mestrado} - Tema da Tese: {aluno_mestrado.tema_tese}")

def verificar_bi_cc_duplicado(bi_cc):
    if bi_cc in dados_alunos.bi_cc:
        return True
    return False

def guardar_dados():
    with open('dados_alunos.pkl', 'wb') as arquivo:
        pickle.dump((dados_alunos, dados_alunos_mestrado), arquivo)
    print("Dados guardados com sucesso.")

def carregar_dados():
    global dados_alunos, dados_alunos_mestrado
    try:
        with open('dados_alunos.pkl', 'rb') as arquivo:
            dados_alunos, dados_alunos_mestrado = pickle.load(arquivo)
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("O arquivo de dados não existe.")

def eliminar_ficheiro():
    try:
        os.remove('dados_alunos.pkl')
        print("Ficheiro eliminado com sucesso.")
    except FileNotFoundError:
        print("O arquivo de dados não existe.")

while True:
    print("\nMenu:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Consultar turma")
    print("4. Atualizar dados do aluno")
    print("5. Limpar tela")
    print("6. Guardar os dados no arquivo")
    print("7. Carregar dados do arquivo")
    print("8. Eliminar arquivo de dados")
    print("9. Sair")

    escolha = input("Escolha uma opção (1-9): ")

    if escolha == "1":
        #Adicionar aluno
        while True:
            nome = input("Insira o nome do aluno: ")
            morada = input("Insira a morada do aluno: ")
            while True:
                bi_cc = input("Insira o número do Bilhete de Identidade/Cartão de Cidadão do aluno: ")
                if verificar_bi_cc_duplicado(bi_cc):
                    print("Erro: Número de Bi/CC já existente. Tente novamente.")
                else:
                    break
            telefone = input("Insira o número de telefone do aluno: ")
            email = input("Insira o e-mail do aluno: ")

            #O número do aluno é automaticamente incrementado
            numero = indice_aluno
            indice_aluno += 1

            dados_alunos.nomes.append(nome)
            dados_alunos.moradas.append(morada)
            dados_alunos.bi_cc.append(bi_cc)
            dados_alunos.telefones.append(telefone)
            dados_alunos.emails.append(email)
            dados_alunos.numeros.append(numero)
            print("Aluno adicionado com sucesso!")

            #Pergunta se o aluno está a fazer mestrado
            opcao_mestrado = input("O aluno está a fazer mestrado? (s/n): ")
            if opcao_mestrado.lower() == 's':
                tema_tese = input("Insira o tema da tese de mestrado do aluno: ")
                dados_alunos_mestrado.temas_tese.append(tema_tese)
                print("Dados de mestrado adicionados com sucesso!")

            continuar = input("Deseja continuar a adicionar alunos? (s/n): ")
            if continuar.lower() != 's':
                break

    elif escolha == "2":
        #Remover aluno
        listar_turma()
        if not dados_alunos.nomes:
            print("Não existem alunos na turma.")
        else:
            numero = int(input("Insira o número do aluno que deseja remover: "))
            if numero in dados_alunos.numeros:
                #Encontra o índice do número na lista dos números dos alunos
                indice = dados_alunos.numeros.index(numero)
                #Remove todos os dados do aluno correspondente nas listas
                del dados_alunos.nomes[indice]
                del dados_alunos.moradas[indice]
                del dados_alunos.bi_cc[indice]
                del dados_alunos.telefones[indice]
                del dados_alunos.emails[indice]
                del dados_alunos.numeros[indice]
                print("Aluno de graduação removido com sucesso!")

                #Remove os dados de mestrado se existirem
                if indice < len(dados_alunos_mestrado.alunos_mestrado):
                    del dados_alunos_mestrado.temas_tese[indice]
                    print("Dados de mestrado removidos com sucesso!")

                #Atualiza os números dos alunos após a remoção
                atualizar_numeros_alunos()

            else:
                print("Aluno não encontrado.")

    elif escolha == "3":
        #Consultar turma
        listar_turma()

    elif escolha == "4":
        #Atualizar dados do aluno
        listar_turma()
        if not dados_alunos.nomes:
            print("A turma está vazia. Não há alunos para atualizar os dados.")
        else:
            numero_aluno = int(input("Insira o número do aluno cujos dados deseja atualizar: "))
            if numero_aluno in dados_alunos.numeros:
                indice = dados_alunos.numeros.index(numero_aluno)
                print("Escolha o dado que deseja atualizar:")
                print("1. Nome")
                print("2. Morada")
                print("3. Número de Bilhete de Identidade/Cartão de Cidadão")
                print("4. Número de Telefone")
                print("5. E-mail")
                print("6. Tema da Tese (Aluno de Mestrado)")
                opcao = input("Escolha uma opção (1-6): ")
                if opcao == "1":
                    novo_nome = input("Insira o novo nome do aluno: ")
                    dados_alunos.nomes[indice] = novo_nome.capitalize()
                    print("Nome do aluno atualizado com sucesso.")
                elif opcao == "2":
                    nova_morada = input("Insira a nova morada do aluno: ")
                    dados_alunos.moradas[indice] = nova_morada.upper()
                    print("Morada do aluno atualizada com sucesso.")
                elif opcao == "3":
                    novo_bi_cc = input("Insira o novo número de Bilhete de Identidade/Cartão de Cidadão do aluno: ")
                    if verificar_bi_cc_duplicado(novo_bi_cc):
                        print("Erro: Número de Bi/CC já existente. Tente novamente.")
                    else:
                        dados_alunos.bi_cc[indice] = novo_bi_cc
                        print("Número de Bilhete de Identidade/Cartão de Cidadão do aluno atualizado com sucesso.")
                elif opcao == "4":
                    novo_telefone = input("Insira o novo número de telefone do aluno: ")
                    dados_alunos.telefones[indice] = novo_telefone
                    print("Número de telefone do aluno atualizado com sucesso.")
                elif opcao == "5":
                    novo_email = input("Insira o novo e-mail do aluno: ")
                    dados_alunos.emails[indice] = novo_email.lower()
                    print("E-mail do aluno atualizado com sucesso.")
                elif opcao == "6":
                    if indice - 1 < len(dados_alunos_mestrado.temas_tese):
                        novo_tema_tese = input("Insira o novo tema da tese de mestrado do aluno: ")
                        dados_alunos_mestrado.temas_tese[indice - 1] = novo_tema_tese
                        print("Tema da Tese do aluno de mestrado atualizado com sucesso.")
                    else:
                        print("Aluno não está a tirar mestrado ou não tem tema de tese definido.")
                else:
                    print("Opção inválida. Escolha uma opção de 1 a 6.")
            else:
                print("Aluno não encontrado.")

    elif escolha == "5":
        #Código para limpar a tela (Google Colab)
        clear_output()

    elif escolha == "6":
        # Guardar os dados em um arquivo
        guardar_dados()

    elif escolha == "7":
        # Carregar os dados de um arquivo
        carregar_dados()

    elif escolha == "8":
        # Eliminar o arquivo de dados
        eliminar_ficheiro()

    elif escolha == "9":
        print("Programa Terminado. Obrigado!")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 9.")
