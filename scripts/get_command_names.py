import os
import yaml

DATA_DIR = '/Users/tmskss/Development/ManPageSum/data/'
MAN_PAGES_FILENAME = 'man_pages.yaml'
COMMAND_NAMES_FILENAME = 'command_names.yaml'

with open(DATA_DIR + MAN_PAGES_FILENAME, 'r')  as yaml_file:
    man_pages = yaml.safe_load(yaml_file)

command_names = []

for item in man_pages:
    command_names.append(item['command'])

with open(DATA_DIR+COMMAND_NAMES_FILENAME, 'w') as yaml_file:
    yaml.dump(command_names, yaml_file)
