# pip install sudachipy
# pip install pytesseract
# pip install Pillow
# pip install sudachidict_core

import re
import pytesseract
from sudachipy import dictionary

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



def image_reader(img):
    text = pytesseract.image_to_string(img, lang='jpn')
    return text

def tokenize_japanese_sudachi(s_text):
    tokenizer_obj = dictionary.Dictionary().create()
    tokens = [m.surface() for m in tokenizer_obj.tokenize(s_text)]
    tokens = [token for token in tokens if token != '\n']

    symbols = set('()=?!"#$%&\'*+,-./:;<=>@[\\]^_`{|}~0123456789 「」、abcçdefgğhıijklmnoöprqsştuüxvwyzABCÇDEFGĞHIİJKLMOÖPRQSŞTUÜVXWYZ・')

    tokens = [token for token in tokens if not all(char in symbols for char in token)]


    return tokens


def remove_parentheses(tokens):
    cleaned_tokens = []
    for token in tokens:
        index = token.find('(')
        if index != -1:
            cleaned_token = token[:index]
        else:
            cleaned_token = token
        cleaned_tokens.append(cleaned_token)

    return cleaned_tokens


def filter_kana(tokens):
    filtered_tokens = []
    for token in tokens:
        if re.match(r'^[\u3040-\u309F]+$', token):
            continue
        elif re.match(r'^[\u30A1-\u30F6]+$', token):
            continue
        else:
            filtered_tokens.append(token)

    return filtered_tokens

