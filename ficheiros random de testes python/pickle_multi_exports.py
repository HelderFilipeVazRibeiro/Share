import os
import pickle
import csv
import xml.etree.ElementTree as ET
#from docx import Document
from google.colab import files
from IPython.display import clear_output

class Telemovel:
    def __init__(self, num_serie, marca, modelo, cor):
        self.num_serie = num_serie
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

numeros_serie = []
marcas = []
modelos = []
cores = []

adicionar_hashtag = lambda num_serie: '#' + num_serie
capitalize_marca = lambda marca: marca.capitalize()
lower_modelo = lambda modelo: modelo.lower()

def limpar_ecra():
    clear_output(wait=True)

def listar_telemoveis():
    if not numeros_serie:
        print("\nNenhum telemóvel registado.")
    else:
        print("\nTelemóveis Registados:")
        for i in range(len(numeros_serie)):
            print("Nº de Série: {}, Marca: {}, Modelo: {}, Cor: {}".format(numeros_serie[i], marcas[i], modelos[i], cores[i]))

def adicionar_telemovel():
    num_serie = input("Introduza o Nº de Série do telemóvel: ")
    num_serie = adicionar_hashtag(num_serie)

    if num_serie in numeros_serie:
        print("Erro: Nº de Série já existe!")
        return

    marca = input("Introduza a marca do telemóvel: ")
    marca = capitalize_marca(marca)
    modelo = input("Introduza o modelo do telemóvel: ")
    modelo = lower_modelo(modelo)
    cor = input("Introduza a cor do telemóvel: ").capitalize()

    telemovel = Telemovel(num_serie=num_serie, marca=marca, modelo=modelo, cor=cor)

    numeros_serie.append(telemovel.num_serie)
    marcas.append(telemovel.marca)
    modelos.append(telemovel.modelo)
    cores.append(telemovel.cor)

    print("Telemóvel registado com sucesso!")

def alterar_telemovel():
    listar_telemoveis()
    num_serie = input("Introduza o Nº de Série do telemóvel que deseja alterar: ")

    if num_serie in numeros_serie:
        index = numeros_serie.index(num_serie)
        nova_marca = input("Introduza a nova marca para o telemóvel (anterior: {}): ".format(marcas[index]))
        nova_marca = capitalize_marca(nova_marca)
        novo_modelo = input("Introduza o novo modelo para o telemóvel (anterior: {}): ".format(modelos[index]))
        novo_modelo = lower_modelo(novo_modelo)
        novo_cor = input("Introduza a nova cor para o telemóvel (anterior: {}): ".format(cores[index])).capitalize()

        marcas[index] = nova_marca
        modelos[index] = novo_modelo
        cores[index] = novo_cor
        print("Telemóvel alterado com sucesso!")
    else:
        print("Nº de Série não encontrado.")

def excluir_telemovel():
    listar_telemoveis()
    num_serie = input("Introduza o Nº de Série do telemóvel que deseja excluir: ")

    if num_serie in numeros_serie:
        index = numeros_serie.index(num_serie)
        numeros_serie.pop(index)
        marcas.pop(index)
        modelos.pop(index)
        cores.pop(index)
        print("Telemóvel excluído com sucesso!")
    else:
        print("Nº de Série não encontrado.")

def guardar_dados():
    dados = {
        'numeros_serie': numeros_serie,
        'marcas': marcas,
        'modelos': modelos,
        'cores': cores,
    }
    with open('dados_telemoveis.pkl', 'wb') as file:
        pickle.dump(dados, file)
    print("Dados guardados com sucesso!")

def exportar_csv():
    #Aqui vamos "buscar" o dicionário para exportar
    dados = {
        'numeros_serie': numeros_serie,
        'marcas': marcas,
        'modelos': modelos,
        'cores': cores,
    }
    #Aqui vamos "chamar" o ficheiro/arquivo em modo 'w' (write)
    #A adição de newline='' ao abrir um arquivo em Python, no modo texto,
    #permite controlar manualmente a forma como as quebras de linha são tratadas
    #durante a escrita. Isto é útil para garantir a consistência, especialmente ao lidar com arquivos CSV,
    #sendo desejável controlar explicitamente o formato das quebras de linha, independentemente do sistema operativo.
    with open('dados_telemoveis.csv', 'w', newline='') as file:
        #Tendo importado a biblioteca/módulo CSV no Python através do comando
        #'writer' vamos gerar o ficheiro csv
        writer = csv.writer(file)
        #Aqui vamos definir o cabeçalho do ficheiro, ou seja, indicar de que forma
        #Vão ser gerados os títulos das tabelas
        writer.writerow(['Nº de Série', 'Marca', 'Modelo', 'Cor'])
        #Vamos escrever os dados de acordo com os que foram registados na lista
        for i in range(len(numeros_serie)):
            #E aqui ele escreve/guarda os dados no ficheiro
            writer.writerow([numeros_serie[i], marcas[i], modelos[i], cores[i]])

    print("Dados exportados para CSV com sucesso.")

def exportar_xml():
    #'ET' vem de Element Tree
    #Nesta linha estamos a criar um elemento de raíz para o documento XML com o
    #Nome 'telemóveis'
    root = ET.Element("telemoveis")
    #Aqui iteramos todos os elementos através do ID principal(nº de série)
    for i in range(len(numeros_serie)):
        telemovel = ET.SubElement(root, "telemovel")
        #Aqui criamos os subelementos dentro do elemento de raíz
        ET.SubElement(telemovel, "num_serie").text = numeros_serie[i]
        ET.SubElement(telemovel, "marca").text = marcas[i]
        ET.SubElement(telemovel, "modelo").text = modelos[i]
        ET.SubElement(telemovel, "cor").text = cores[i]

    #Aqui criamos uma nova árvore XML com o elemento de raíz
    tree = ET.ElementTree(root)
    #E aqui vamos escrever/guardar o ficheiro XML com os dados correspondentes
    tree.write("dados_telemoveis.xml")
    print("Dados exportados para XML com sucesso.")

#def exportar_doc():
    #Aqui criamos um novo documento Docx, sendo representado neste exemplo por
    #'doc'
    #doc = Document()
    #Aqui adicionamos um título ao documento, sendo "Dados dos Telemóveis" sendo
    #O '0' o nível de cabeçalho a ser criado
   # doc.add_heading('Dados dos Telemóveis', 0)
    #Aqui iteramos os dados com o índice
   #for i in range(len(numeros_serie)):
        #Aqui criamos no documento um parágrafo com as informações dos telemóveis
        #doc.add_paragraph("Nº de Série: {}, Marca: {}, Modelo: {}, Cor: {}".format(numeros_serie[i], marcas[i], modelos[i], cores[i]))
    #Por fim guardamos/geramos o ficheiro
    #doc.save('dados_telemoveis.docx')
    #print("Dados exportados para DOC com sucesso.")

def download_arquivo_csv():
    files.download('dados_telemoveis.csv')

def download_arquivo_xml():
    files.download('dados_telemoveis.xml')

#def download_arquivo_doc():
    #files.download('dados_telemoveis.docx')

def carregar_dados():
    global numeros_serie, marcas, modelos, cores
    try:
        with open('dados_telemoveis.pkl', 'rb') as file:
            dados = pickle.load(file)
        numeros_serie = dados['numeros_serie']
        marcas = dados['marcas']
        modelos = dados['modelos']
        cores = dados['cores']
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Ficheiro não encontrado.")

def apagar_dados():
    try:
        os.remove('dados_telemoveis.pkl')
        print("Dados apagados com sucesso!")
    except FileNotFoundError:
        print("Ficheiro não encontrado.")

carregar_dados()

while True:
    print("\nMenu:")
    print("1. Registar Telemóvel")
    print("2. Listar Telemóveis")
    print("3. Alterar Telemóvel")
    print("4. Excluir Telemóvel")
    print("5. Limpar Tela")
    print("6. Guardar Dados")
    print("7. Carregar Dados")
    print("8. Apagar Dados")
    print("9. Exportar para CSV")
    print("10. Exportar para XML")
    #print("11. Exportar para DOC")
    print("11. Download CSV")
    print("12. Download XML")
    #print("14. Download DOC")
    print("13. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_telemovel()
    elif opcao == "2":
        listar_telemoveis()
    elif opcao == "3":
        alterar_telemovel()
    elif opcao == "4":
        excluir_telemovel()
    elif opcao == "5":
        limpar_ecra()
    elif opcao == "6":
        guardar_dados()
    elif opcao == "7":
        carregar_dados()
    elif opcao == "8":
        apagar_dados()
    elif opcao == "9":
        exportar_csv()
    elif opcao == "10":
        exportar_xml()
    #elif opcao == "11":
        exportar_doc()
    elif opcao == "11":
        download_arquivo_csv()
    elif opcao == "12":
        download_arquivo_xml()
   # elif opcao == "14":
        download_arquivo_doc()
    elif opcao == "13":
        print("A sair do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
