import os
import csv
import sys

DATA_DIR = '/Users/tmskss/Development/ManPageSum/data/'
DATASET_FILENAME = 'dataset.csv'

csv.field_size_limit(sys.maxsize)

data = []
with open(DATA_DIR + DATASET_FILENAME, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        data.append(row)

count = 0
for row in data:
    if row[1] != '':
        count += 1
    
print(count)
