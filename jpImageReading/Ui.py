import sys

import tkinter as tk
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap





def screenLayer():
    def on_click(event):
        root.destroy()
    root = tk.Tk()

    root.overrideredirect(True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.title('KanjiReader')
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-topmost', True)  # Make the overlay window always on top
    root.attributes('-alpha', 0.15)  # Set transparency level (0.0 to 1.0)

    canvas = tk.Canvas(root, bg='gray', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)


    canvas.bind('<ButtonRelease-1>', on_click)
    root.mainloop()







def textUi(translated_text):


    app = QApplication(sys.argv)

    ui = loadUi('Text.ui')
    #ui.actionClose.triggered.connect(ui.hide())
    #ui.actionQuit.triggered.connect(ui.exit())


    def nextKanji():
        if len(translated_text) == 0:
            ui.textBox.setText("Could not read message")
        elif len(translated_text) == iKanji:
            ui.textBox.setText(translated_text[iKanji % len(translated_text)])
        else:
            ui.textBox.setText(translated_text[iKanji])

    def prevKanji():
        if len(translated_text) == 0:
            ui.textBox.setText("Could not read message")
        elif len(translated_text) == iKanji-jKanji:
            ui.textBox.setText(translated_text[iKanji-jKanji % len(translated_text)])
        else:
            ui.textBox.setText(translated_text[iKanji-jKanji])


    img = QPixmap('screenshot.png')
    if(img.width() > 120):
        ui.resize(img.width() + 80, img.height() + 160)
        ui.image.resize(img.width(), img.height())
        ui.textBox.move(0, img.height())
        ui.textBox.resize(img.width(), 65)
        ui.prevButton.move(int(img.width() / 4), int(img.height() + 80))
        # not added
        # ui.copyButton(int(img.width()/2), int(img.height() + 50))
        ui.nextButton.move(int(img.width() * 3 / 4), int(img.height() + 80))



    ui.image.setPixmap(img)
    if len(translated_text) == 0:
        ui.textBox.setText("Could not read message")
    else:
        ui.textBox.setText(translated_text[0])


    global iKanji, jKanji
    iKanji, jKanji = 0, 0
#implement next/prev/copy buttons
    if(ui.nextButton.clicked.connect(nextKanji)) :
        iKanji += 1

    if (ui.prevButton.clicked.connect(prevKanji)):
        jKanji += 1

    ui.show()
    sys.exit(app.exec_())
