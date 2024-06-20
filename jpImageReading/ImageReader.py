# pip install sudachipy
# pip install pytesseract
# pip install Pillow
# pip install sudachidict_core

import re
import pytesseract
from PIL import Image
from sudachipy import tokenizer
from sudachipy import dictionary

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



#image_path = 'jpread3.png'
#img = Image.open(image_path)
#text = pytesseract.image_to_string(img, lang='jpn')
#print(text)
#tokenizer_obj = dictionary.Dictionary().create()


def image_reader(img):
    #img = Image.open(path)
    text = pytesseract.image_to_string(img, lang='jpn')
    return text

# Define a function to tokenize Japanese text using SudachiPy
def tokenize_japanese_sudachi(s_text):
    tokenizer_obj = dictionary.Dictionary().create()
    # Tokenize the text
    tokens = [m.surface() for m in tokenizer_obj.tokenize(s_text)]
    tokens = [token for token in tokens if token != '\n']

    # Define symbols that you want to filter out
    symbols = set('()=?!"#$%&\'*+,-./:;<=>@[\\]^_`{|}~0123456789 「」、abcçdefgğhıijklmnoöprqsştuüxvwyzABCÇDEFGĞHIİJKLMOÖPRQSŞTUÜVXWYZ・')

    # Filter out tokens that consist solely of symbols or start/end with symbols
    tokens = [token for token in tokens if not all(char in symbols for char in token)]


    return tokens


def remove_parentheses(tokens):
    cleaned_tokens = []
    for token in tokens:
        # Find the index of '('
        index = token.find('(')
        if index != -1:
            # Extract text before '('
            cleaned_token = token[:index]
        else:
            # If '(' is not found, use the original token
            cleaned_token = token

        # Append cleaned token to the result list
        cleaned_tokens.append(cleaned_token)

    return cleaned_tokens


def filter_hiragana_only(tokens):
    filtered_tokens = []
    for token in tokens:
        # Check if the token consists only of hiragana characters
        if re.match(r'^[\u3040-\u309F]+$', token):  # Range for hiragana characters in Unicode
            continue  # Skip adding hiragana-only tokens to the filtered list
        else:
            filtered_tokens.append(token)

    return filtered_tokens



# Example usage
#japanese_text = text
#tokens = tokenize_japanese_sudachi(japanese_text)
#filtered_tokens = filter_hiragana_only(tokens)
#cleaned_tokens = remove_parentheses(filtered_tokens)
#print(cleaned_tokens)