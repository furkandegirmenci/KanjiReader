import sys

import tkinter as tk
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton


def initUI(kanji, meanings):
    # Create the application object
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle('Copyable Text Example')

    # Create a layout for the main window
    layout = QVBoxLayout(window)

    # Create a QTextEdit widget to display copyable text
    text_edit = QTextEdit()
    clean_meanings = ', '.join(meanings)


    text_edit.setPlainText(f'{kanji}\n\n{clean_meanings}')
    text_edit.setReadOnly(True)  # Make the text read-only
    layout.addWidget(text_edit)

    # Create a button to copy text
    copy_button = QPushButton('Copy Text')
    copy_button.clicked.connect(lambda: text_edit.selectAll())
    layout.addWidget(copy_button)

    # Set the layout for the main window
    window.setLayout(layout)

    # Show the main window
    window.show()

    # Execute the application's event loop
    app.exec_()





def screenLayer():
    def on_click(event):
        root.destroy()
    # Create the root window
    root = tk.Tk()

    root.overrideredirect(True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set properties of the root window
    root.title('KanjiReader')
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-topmost', True)  # Make the overlay window always on top
    root.attributes('-alpha', 0.15)  # Set transparency level (0.0 to 1.0)

    # Create a canvas to draw on
    canvas = tk.Canvas(root, bg='gray', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Start the Tkinter event loop

    canvas.bind('<ButtonRelease-1>', on_click)
    root.mainloop()




