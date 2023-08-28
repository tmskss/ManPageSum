import os
import yaml
import csv

DATA_DIR = '/Users/tmskss/Development/ManPageSum/data/'
TLDR_PAGES_FILENAME = 'tldr_pages.yaml'
MAN_PAGES_FILENAME = 'man_pages.yaml'
COMMAND_NAMES_FILENAME = 'command_names.yaml'

DATASET_FILENAME = 'dataset.csv'

with open(DATA_DIR + TLDR_PAGES_FILENAME, 'r')  as yaml_file:
    tldr_pages = yaml.safe_load(yaml_file)

tldr_dict = dict()
for item in tldr_pages:
    tldr_dict[item['command']] = item['text']

with open(DATA_DIR + MAN_PAGES_FILENAME, 'r')  as yaml_file:
    man_pages = yaml.safe_load(yaml_file)

man_pages_dict = dict()
for item in man_pages:
    man_pages_dict[item['command']] = item['text']

with open(DATA_DIR + COMMAND_NAMES_FILENAME, 'r')  as yaml_file:
    command_names = yaml.safe_load(yaml_file)

data = []
for command in command_names:
    if command not in tldr_dict:
        tldr_dict[command] = ''
    data.append(('summarize: ' + man_pages_dict[command], tldr_dict[command]))


with open(DATA_DIR + DATASET_FILENAME, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Text", "Summary"])  # Writing header row
    csv_writer.writerows(data)       # Writing the list of pairs