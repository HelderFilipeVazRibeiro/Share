# Importa as bibliotecas necessárias
import math  # <---- bibliteca com funcções matemáticas

# Define as entradas do algoritmo
locais_plantacao = [[1, 2], [3, 4]] # <---- Variaveis int dentro de uma array
fontes_agua = ["Rio", "Lago", "Poço"]# <---- Variaveis str dentro de uma array
recursos_financeiros = 10000 # <---- atribuição de um valor a uma variavel 
recursos_humanos = 10 # <---- atribuição de um valor a uma variavel

# Define as variáveis de saída
fonte_agua_mais_proxima = None #<---- inicialização da variavel
projeto_canal = None #<---- inicialização da variavel
instalacoes_bombas = None #<---- inicialização da variavel

# Identifica as fontes de água disponíveis na região
fontes_agua_disponiveis = [] # <-- variavel com array
for local_plantacao in locais_plantacao: # <--- ciclo for "até"
    fonte_agua_str = map(str, local_plantacao) # <--- usa a função map() para converter a lista de números local_plantacao em uma lista de strings
    for fonte_agua in fonte_agua_str: # <--- até que  
        if fonte_agua in fonte_agua: # <--- se  
            fontes_agua_disponiveis.append(fonte_agua) # <-- Adiciona fonte_agua à array fontes_agua_disponiveis

# Avalia as características das fontes de água disponíveis
for fonte_agua in fontes_agua_disponiveis: # para fonte_agua em fontes_agua_disponiveis
    # Obtém as informações sobre a qualidade da água
    qualidade_agua = "potável" # <---- Variaveis str
    # Obtém as informações sobre a vazão da água
    vazao_agua = 100 # <---- Variaveis int 
    # Obtém as informações sobre a distância da fonte das plantações
    distancia_fonte_plantacao = 10 # <---- Variaveis int 

# Identifica a fonte de água mais próxima que atenda às necessidades das plantações
for fonte_agua in fontes_agua_disponiveis: # <--- ciclo for, até
    if qualidade_agua == "potável" and vazao_agua >= 100: # qualidade_agua é igual "potável" e vazao_agua maior ou igual a 100
        fonte_agua_mais_proxima = fonte_agua # <-- atribui o valor de fonte_agua à variavel fonte_agua_mais_proxima
        break # para o programa quando maior ou igual a 100

# Projeta o canal
tamanho_canal = math.ceil(vazao_agua / distancia_fonte_plantacao) # <--- vazao_agua / distancia_fonte_ plantacao. math ceil arredonda um valor para cima. passa o valor para a variavel tamanho_canal
material_canal = "cimento" # <---- Variavel str
relevo_canal = "plano" # <---- Variavel str

# Constrói o canal
projeto_canal = {"tamanho": tamanho_canal, "material": material_canal, "relevo": relevo_canal} # <---- cria um dicionário projeto_canal com tamanho, material e relevo

# Instala as bombas
tipo_bomba = "elétrica" # <---- Variavel str
potencia_bomba = 1000 # <---- Variavel int
quantidade_bombas = math.ceil(distancia_fonte_plantacao / 10) # <--- distancia_fonte_plantacao / 10 . math ceil arredonda um valor para cima. passa o valor para quantidade_bombas

# Instala as bombas de forma segura e eficiente
instalacoes_bombas = {"tipo": tipo_bomba, "potencia": potencia_bomba, "quantidade": quantidade_bombas}# <---- cria um dicionário

# Testa o sistema de irrigação
vazao_agua_teste = 100 # <---- Variavel str
pressao_agua_teste = 10 # <---- Variavel str
funcionamento_bombas_teste = True # <---- Variavel boleana

# Verifica a vazão da água
if vazao_agua_teste != vazao_agua:# <---- se vazao_agua_teste diferente de vazao_agua
    raise Exception("Vazao da água não corresponde ao projeto") #<-- exceção do tipo Exception com a mensagem "Vazao da água não corresponde ao projeto"

# Verifica a pressão da água
if pressao_agua_teste != 10: # <---- se pressao_agua_teste diferente de 10
    raise Exception("Pressão da água não corresponde ao projeto") #<-- exceção do tipo Exception com a mensagem "Vazao da água não corresponde ao projeto"

# Verifica o funcionamento das bombas
if funcionamento_bombas_teste is False: #<--- se funcionamento_bombas_teste for falso
    raise Exception("Bombas não estão funcionando corretamente") #<-- exceção do tipo Exception com mensagem "Bombas não estão funcionando corretamente"

# Imprime as saídas do algoritmo
print("Fonte de água mais próxima:", fonte_agua_mais_proxima) # <--- saída de dados 
print("Projeto do canal:", projeto_canal) # <--- saída de dados 
print("Instalações das bombas:", instalacoes_bombas) # <--- saída de dados 