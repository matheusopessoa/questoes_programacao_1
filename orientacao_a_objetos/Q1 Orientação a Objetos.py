class Playlist:
    def __init__(self, name, genre, songs):
        self.name = name
        self.genre = genre
        self.songs = songs

    def add(self, song):
        self.songs.append(song)

    def remove(self):
        self.songs.pop()

    def play(self):
        print(f'Play em {self.name}')
        for element in self.songs:
            print(f'Tocando {element}...')
        print(f'Essa festa foi um sucesso!')

    def duration(self):
        return len(self.songs) * 3

def adjust_playlist():
    current_duration = playlist_obj.duration()
    songs_added = 0
    songs_removed = 0

    while current_duration > party_duration + 2:
        playlist_obj.remove()
        current_duration = playlist_obj.duration()
        songs_removed += 1

    while current_duration + 2 < party_duration:
        current_duration += 3
        songs_added += 1

    return songs_added, songs_removed

def correct_playlist(songs_needed, songs_excess):
    if songs_needed > 0:
        print(f'Precisaremos adicionar mais {songs_needed} músicas a playlist {playlist_obj.name}')
        for i in range(songs_needed):
            song = input()
            playlist_obj.songs.append(song)
    if songs_excess > 0:
        print(f'Precisaremos remover {songs_excess} músicas da playlist {playlist_obj.name}')

playlist_list = []

num_playlists = int(input())

for i in range(num_playlists):
    name = input()
    genre = input()
    songs = input().split(', ')
    playlist_obj = Playlist(name, genre, songs)
    playlist_list.append(playlist_obj)

genre_played = input()
party_duration = int(input())
found_playlist = False

for i, playlist_obj in enumerate(playlist_list):
    if playlist_obj.genre == genre_played:
        songs_needed, songs_excess = adjust_playlist()
        correct_playlist(songs_needed, songs_excess)
        playlist_obj.play()
        found_playlist = True

if not found_playlist:
    print(f"Não tenho nenhuma playlist do gênero {genre_played}, infelizmente não poderei tocar")
