# funções
def adicionar_aluno(turma_nomes, turma_notas):
    try:
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
    except ValueError:
        print("Erro: A nota deve ser um número.")
        return

    turma_nomes.append(nome)
    turma_notas.append(nota)
    print(f"Aluno {nome} adicionado com sucesso!")

def remover_aluno(turma_nomes, turma_notas):
    nome = input("Digite o nome do aluno a ser removido: ")
    if nome in turma_nomes:
        try:
            indice = turma_nomes.index(nome)
            turma_nomes.pop(indice)
            turma_notas.pop(indice)
            print(f"Aluno {nome} removido com sucesso!")
        except IndexError:
            print("Erro ao remover o aluno. Índice inválido.")
    else:
        print(f"Aluno {nome} não encontrado na turma.")

def atualizar_dados_aluno(turma_nomes, turma_notas):
    nome = input("Digite o nome do aluno a ser atualizado: ")
    if nome in turma_nomes:
        try:
            indice = turma_nomes.index(nome)
            nova_nota = float(input("Digite a nova nota do aluno: "))
            turma_notas[indice] = nova_nota
            print(f"Dados do aluno {nome} atualizados com sucesso!")
        except (ValueError, IndexError):
            print("Erro ao atualizar os dados do aluno.")
    else:
        print(f"Aluno {nome} não encontrado na turma.")

def listar_turma(turma_nomes, turma_notas):
    print("\nLista de Alunos:")
    for nome, nota in zip(turma_nomes, turma_notas):
        print(f"Nome: {nome}, Nota: {nota}")
        
# Arrays
turma_nomes = [] #<--- array valores nomes
turma_notas = [] #<--- array valores notas

#enquanto
while True:
    print("\nMenu:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Atualizar dados do aluno")
    print("4. Listar a turma")
    print("5. Terminar Programa")
    opcao = input("\nEscolha uma opção (1-5): ")
    
    # se
    if opcao == "1":
        adicionar_aluno(turma_nomes, turma_notas) #<--- adiciona valor à array nomes e notas
    
    # então se
    elif opcao == "2":
        remover_aluno(turma_nomes, turma_notas) # <--- remove valor à array nomes e notas

    # então se
    elif opcao == "3":
        atualizar_dados_aluno(turma_nomes, turma_notas)

    # então se
    elif opcao == "4":
        listar_turma(turma_nomes, turma_notas)
    
    # então se
    elif opcao == "5":
        print("Programa terminado...3...2...1...0")
        break
    
    # senão
    else:
        print("Por favor, escolha uma opção valida!")