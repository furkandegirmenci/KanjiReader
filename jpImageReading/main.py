print('hi')

import ImageReader
import SsTaker
import Translate

img = SsTaker.takePicture()
text = ImageReader.image_reader(img)
tokens = ImageReader.tokenize_japanese_sudachi(text)
clear_tokens = ImageReader.remove_parentheses(tokens)
complete_tokens = ImageReader.filter_hiragana_only(clear_tokens)
print(complete_tokens)
int = 0
if(len(complete_tokens) != 0):
    for token in complete_tokens:
        Translate.search_japanese_word(token)

print('bye')
