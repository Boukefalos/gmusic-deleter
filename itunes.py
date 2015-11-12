#!/usr/bin/python
# Copyright (c) 2014 Rik Veenboer <rik.veenboer@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from pyItunes import *
from gmusicapi import Mobileclient

# iTunes songs
l = Library('<full path to iTunes Music Library.xml>')
songs = [(song.artist, song.name) for id,song in l.songs.items()]

# Google Music songs
api = Mobileclient()
api.login('<account>', '<password>', Mobileclient.FROM_MAC_ADDRESS)
library = api.get_all_songs()

# Find songs to delete
delete = filter(lambda song: (song['artist'], song['title']) not in songs, library)
delete = [song['id'] for song in delete]

if len(delete):
    # Display songs
    print "Duplicate songs"
    old_song_ids = []
    for key in sorted(delete):
        key = '%s: %d-%02d %s' % (song.get('album'), song.get('discNumber'), song.get('trackNumber'), song.get('title'))
        print "    " + key.encode('utf-8')

    # Delete songs
    if raw_input( "Delete duplicate songs? (y, n): ") is 'y':
        print "Deleting songs..."
        api.delete_songs(delete)
else:
    print 'No deleted songs'