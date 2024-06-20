import sys
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




