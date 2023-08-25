import re
from collections import defaultdict
import os
import yaml

# Path to the directory containing the man pages
man_pages_directory = "/Users/tmskss/Development/ManPageSum/man_txt_files"

# Path of file to write the extracted information to
yaml_file_path = '/Users/tmskss/Development/ManPageSum/data/man_pages.yaml'


def get_description_part(txt):
    cut_token_first = 'NAME'
    
    if '## DESCRIPTION         top' in txt:
        cut_token_first = '## DESCRIPTION         top'
    elif '## OVERVIEW         top' in txt:
        cut_token_first = '## OVERVIEW         top'
    elif '## INTRODUCTION         top' in txt:
        cut_token_first = '## INTRODUCTION         top'
    elif '## Description         top' in txt:
        cut_token_first = '## Description         top'
    elif '## Overview         top' in txt:
        cut_token_first = '## Overview         top'
    elif '## Introduction         top' in txt:
        cut_token_first = '## Introduction         top'


    if cut_token_first == 'NAME':
        description_part = txt
    else:
        first_part = txt.split(cut_token_first)[1]
        description_part = first_part.split('##')[0] if '##' in first_part else first_part

    return description_part

def get_options_part(txt):
    if '## OPTIONS         top' in txt:
        first_part = txt.split('## OPTIONS         top')[1]
        options_part = first_part.split('##')[0] if '##' in first_part else first_part
    elif '## Options         top' in txt:
        first_part = txt.split('## Options         top')[1]
        options_part = first_part.split('##')[0] if '##' in first_part else first_part
    else:
        options_part = ''
    
    return options_part

def clean_string(input_string):
    # Remove newline characters
    cleaned_string = input_string.replace("\n", " ")
    
    # Replace multiple whitespace characters with a single space
    cleaned_string = re.sub(r"\s+", " ", cleaned_string)
    
    return cleaned_string

# Dictionary to store extracted information
man_page_data = []

# Regular expression pattern to identify command names in the man page filenames
command_name_pattern = re.compile(r'^([a-z0-9-]+)\.\d$')


# Extract information from man pages
for filename in os.listdir(man_pages_directory):
    command_name = filename.split('.')[0]
    with open(os.path.join(man_pages_directory, filename), 'r') as f:
        man_page_content = f.read()
        
        # Extract relevant sections (description, options)
        desc = get_description_part(man_page_content)
        options = get_options_part(man_page_content)

        full_text = desc + '\n' + options

        clean_txt = clean_string(full_text)

        man_page_data.append({'command': command_name, 'text': clean_txt})
        
with open(yaml_file_path, 'w') as yaml_file:
    yaml.dump(man_page_data, yaml_file)



