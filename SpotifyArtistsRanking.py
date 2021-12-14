import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

print("Introduce la URL de la playlist que desees")
playlist_id=input()
playlist_id = 'https://open.spotify.com/playlist/0Vp35h337JHQCOPgKjoh4N?si=4efcbe460bbe49c6'
results = sp.playlist(playlist_id)
diccionarioArtistas = {}

for item in results['tracks']['items']:
    nombre = (item['track']['artists'][0]['name'])
    url = (item['track']['artists'][0]['external_urls']['spotify'])
    artista = sp.artist(url)
    popularity = artista.get('popularity')
    diccionarioArtistas[nombre] = popularity
    
sorted_artistas = sorted(diccionarioArtistas.items(), key=lambda x: x[1], reverse=True)

print ("{:<18} {:<10}".format('ARTISTA', 'POPULARIDAD'))
for i in sorted_artistas:
	print("{:<18} {:<10}".format(i[0], i[1]))