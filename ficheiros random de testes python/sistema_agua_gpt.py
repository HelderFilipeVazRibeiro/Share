# Importa a biblioteca necessária
import math

# Define as entradas do algoritmo
locais_plantacao = [[1, 2], [3, 4]]  # Coordenadas dos locais de plantação
fontes_agua = ["Rio", "Lago", "Poço"]  # Tipos de fontes de água disponíveis
recursos_financeiros = 10000  # Recursos financeiros disponíveis
recursos_humanos = 10  # Recursos humanos disponíveis

# Define as variáveis de saída
fonte_agua_mais_proxima = None  # Inicializa a fonte de água mais próxima como Nulo
projeto_canal = None  # Inicializa o projeto do canal como Nulo
instalacoes_bombas = None  # Inicializa as instalações das bombas como Nulo

# Identifica as fontes de água disponíveis na região
fontes_agua_disponiveis = []
for fonte_agua in fontes_agua:
    for local_plantacao in locais_plantacao:
        if fonte_agua.startswith(str(local_plantacao[0])):
            fontes_agua_disponiveis.append(fonte_agua)

# Avalia as características das fontes de água disponíveis
for fonte_agua in fontes_agua_disponiveis:
    # Obtém as informações sobre a qualidade da água
    qualidade_agua = "potável"
    # Obtém as informações sobre a vazão da água
    vazao_agua = 100
    # Obtém as informações sobre a distância da fonte das plantações
    distancia_fonte_plantacao = 10

    # Projeta o canal
    tamanho_canal = math.ceil(vazao_agua / distancia_fonte_plantacao)
    material_canal = "cimento"
    relevo_canal = "plano"

    # Constrói o canal
    projeto_canal = {"tamanho": tamanho_canal, "material": material_canal, "relevo": relevo_canal}

    # Instala as bombas
    tipo_bomba = "elétrica"
    potencia_bomba = 1000
    quantidade_bombas = math.ceil(distancia_fonte_plantacao / 10)

    # Instala as bombas de forma segura e eficiente
    instalacoes_bombas = {"tipo": tipo_bomba, "potencia": potencia_bomba, "quantidade": quantidade_bombas}

    # Testa o sistema de irrigação
    vazao_agua_teste = 100
    pressao_agua_teste = 10
    funcionamento_bombas_teste = False  # Definido como False para teste

    # Verifica a vazão da água
    if vazao_agua_teste != vazao_agua:
        raise Exception("Vazão da água não corresponde ao projeto")

    # Verifica a pressão da água
    if pressao_agua_teste != 10:
        raise Exception("Pressão da água não corresponde ao projeto")

    # Verifica o funcionamento das bombas
    if not funcionamento_bombas_teste:
        raise Exception("Bombas não estão funcionando corretamente")

# Imprime as saídas do algoritmo
print("Fonte de água mais próxima:", fonte_agua)
print("Projeto do canal:", projeto_canal)
print("Instalações das bombas:", instalacoes_bombas)
