from pyItunes import *
from gmusicapi import Mobileclient

# iTunes songs
l = Library("<full path to iTunes Music Library.xml>")
songs = [(song.artist, song.name) for id,song in l.songs.items()]

# Google Music songs
api = Mobileclient()
api.login('<account>', '<password>')
library = api.get_all_songs()

# Find songs to delete
delete = filter(lambda song: (song['artist'], song['title']) not in songs, library)
delete = [song['id'] for song in delete]

# Delete songs
api.delete_songs(delete)