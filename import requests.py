import requests

def buscar_informacoes_musica(artist_name, track_name):
    # Parâmetros da busca na API do iTunes
    params = {
        'term': f'{artist_name} {track_name}',
        'media': 'music',
        'entity': 'musicTrack',
        'limit': 1  # Limita a busca a 1 resultado
    }

    # URL da API do iTunes
    url = 'https://itunes.apple.com/search'

    # Faz a requisição GET para a API do iTunes
    response = requests.get(url, params=params)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Converte a resposta para JSON
        resultados = response.json()

        # Verifica se há resultados
        if resultados['resultCount'] > 0:
            # Obtém a primeira música da lista de resultados
            musica = resultados['results'][0]

            # Exibe as informações da música
            print(f"Artista: {musica['artistName']}")
            print(f"Nome da música: {musica['trackName']}")
            print(f"Álbum: {musica['collectionName']}")
            print(f"Data de lançamento: {musica['releaseDate']}")
        else:
            print("Nenhum resultado encontrado.")
    else:
        print(f"Erro na requisição. Código: {response.status_code}")

# Exemplo de uso
buscar_informacoes_musica('Ed Sheeran', 'Shape of You')
