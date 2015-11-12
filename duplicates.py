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

from gmusicapi import Mobileclient

# Login
api = Mobileclient()
api.login('<account>', '<password>', Mobileclient.FROM_MAC_ADDRESS)

# Google Music songs
print 'Getting all songs ...'
all_songs = api.get_all_songs()
new_songs = {}
old_songs = {}

# Find duplicates
for song in all_songs:
    song_id = song.get('id')
    timestamp = song.get('recentTimestamp')
    key = '%s: %d-%02d %s' % (song.get('album'), song.get('discNumber'), song.get('trackNumber'), song.get('title'))    
    if key in new_songs:
        if new_songs[key]['timestamp'] < timestamp:
            old_songs[key] = new_songs[key]
            new_songs[key] = {'id': song_id, 'timestamp': timestamp}
        else:
            old_songs[key] = {'id': song_id, 'timestamp': timestamp}    
    new_songs[key] = {'id': song_id, 'timestamp': timestamp}

if len(old_songs):
    # Display songs
    print 'Duplicate songs'
    delete = []
    for key in sorted(old_songs.keys()):
        delete.append(old_songs[key]['id'])
        print '    ' + key.encode('utf-8')

    # Delete songs
    if raw_input( 'Delete duplicate songs? (y, n): ') is 'y':
        print 'Deleting songs...'
        api.delete_songs(delete)
else:
    print 'No duplicate songs'