import csv
import subprocess
import os

output_folder = '..\\music'

csv_files = [
    '..\\DataFiles\\output_part_1.csv', '..\\DataFiles\\output_part_2.csv', '..\\DataFiles\\output_part_3.csv', 
    '..\\DataFiles\\output_part_4.csv', '..\\DataFiles\\output_part_5.csv', '..\\DataFiles\\output_part_6.csv', 
    '..\\DataFiles\\output_part_7.csv', '..\\DataFiles\\output_part_8.csv', '..\\DataFiles\\output_part_9.csv', 
    '..\\DataFiles\\output_part_10.csv', '..\\DataFiles\\output_part_11.csv', '..\\DataFiles\\output_part_12.csv'
]

for csv_file in csv_files:
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            track_uri = row[0]
            url = "https://open.spotify.com/track/" + track_uri
            command = ['spotdl', url, '--web-use-output-dir', '--output', output_folder]
            try:
                subprocess.run(command, check=True)
                print(f'Processing: {url}')
            except subprocess.CalledProcessError as e:
                print(f'Failed to process {url}: {e}')
