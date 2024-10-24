import csv
import json
import subprocess

output_folder = 'music'

with open('mpd.slice.7000-7999.json', encoding='utf-8') as f:
    data = json.load(f)
for playlist in data['playlists']:
    for track in playlist['tracks']:
        track_uri = track['track_uri']
        track_id = track_uri.split('spotify:track:')[1]
        url = "https://open.spotify.com/track/" + track_id
        command = ['spotdl', url, '--web-use-output-dir', '--output', output_folder]
        try:
            subprocess.run(command, check=True)
            print(f'Processing: {url}')
        except subprocess.CalledProcessError as e:
            print(f'Failed to process {url}: {e}')