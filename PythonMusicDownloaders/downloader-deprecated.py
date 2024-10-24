import csv
import subprocess

# Define the CSV file path and output folder
csv_file_path = 'C:\\Users\\david\\Downloads\\artisturis.csv'
output_folder = 'C:\\Users\\david\\Downloads\\test'

def download_music_from_spotify(csv_file, output_dir):
    with open(csv_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row:
                url = row[0]
                command = ['spotdl', url, '--web-use-output-dir', '--output', output_dir]
                try:
                    subprocess.run(command, check=True)
                    print(f'Processing: {url}')
                except subprocess.CalledProcessError as e:
                    print(f'Failed to process {url}: {e}')
download_music_from_spotify(csv_file_path, output_folder)