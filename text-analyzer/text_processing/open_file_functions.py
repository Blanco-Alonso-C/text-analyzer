from importlib.resources import files
from data.inputs.examples import *

# To analyze another text, you can change deafult text or paste it on file.txt
def open_file(default = sp_human_only_text_review):

    try:
        text = (files('data.inputs') / 'file.txt').read_text(encoding='utf-8')

        if text == '':
            print('No file found. Default text will be used')
            text = default

    except FileNotFoundError:

        print('No file found. Default text will be used')
        text = default

    return text