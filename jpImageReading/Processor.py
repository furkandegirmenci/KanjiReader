import ImageReader
import SsTaker
import Translate
import Ui


def process():
    img = SsTaker.takePicture()
    text = ImageReader.image_reader(img)
    tokens = ImageReader.tokenize_japanese_sudachi(text)
    clear_tokens = ImageReader.remove_parentheses(tokens)
    complete_tokens = ImageReader.filter_kana(clear_tokens)


    translated_text = []
    if(len(complete_tokens) != 0):
        for token in complete_tokens:
            translated_text.append(Translate.search_japanese_word(token))
    Ui.textUi(translated_text)