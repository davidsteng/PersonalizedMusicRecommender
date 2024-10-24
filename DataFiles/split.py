import csv
import os
import math

def split_csv(input_file, output_dir, num_splits=12):
    os.makedirs(output_dir, exist_ok=True)
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        rows = [[row[0], row[1]] for row in reader]
    total_rows = len(rows)
    rows_per_split = math.ceil(total_rows / num_splits)
    for i in range(num_splits):
        start_index = i * rows_per_split
        end_index = min(start_index + rows_per_split, total_rows)
        split_rows = rows[start_index:end_index]

        output_file = os.path.join(output_dir, f'output_part_{i+1}.csv')
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(split_rows)

        print(f'Saved {output_file}')

input_file = '.\\tracks_features.csv'
output_dir = '.\\'
split_csv(input_file, output_dir)