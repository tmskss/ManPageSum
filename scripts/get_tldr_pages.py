import os
import yaml
import markdown
import html2text

def convert_html_file_to_txt_file(html_text):
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    h.ignore_emphasis = True
    h.ignore_anchors = True
    h.ignore_emoji = True

    txt = h.handle(html_text)
    normalized_txt = remove_empty_lines(txt)

    return normalized_txt

def remove_empty_lines(input_string):
    lines = input_string.splitlines()
    non_empty_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_empty_lines)

TLDR_REPO_DIR = '/Users/tmskss/Development/TLDR_REPO/tldr/pages/'
DATA_DIR = '/Users/tmskss/Development/ManPageSum/data/'
COMMAND_NAMES_FILENAME = 'command_names.yaml'
TLDR_PAGES_FILENAME = 'tldr_pages.yaml'

with open(DATA_DIR + COMMAND_NAMES_FILENAME, 'r')  as yaml_file:
    needed_command_names = yaml.safe_load(yaml_file)


already_gathered_commands = []
tldr_pages = []

for subdir, _, files in os.walk(TLDR_REPO_DIR):
    for filename in files:
        command_name = filename.split('.')[0]
        if command_name in needed_command_names and command_name not in already_gathered_commands:
            with open(os.path.join(subdir, filename), 'r') as f:
                file_content = f.read()
            
            html_text = markdown.markdown(file_content)
            plain_text = convert_html_file_to_txt_file(html_text)
            tldr_pages.append({'command': command_name, 'text': plain_text})
            already_gathered_commands.append(command_name)

with open(DATA_DIR+TLDR_PAGES_FILENAME, 'w') as yaml_file:
    yaml.safe_dump(tldr_pages, yaml_file)