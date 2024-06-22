# KanjiReader
Hi, this is a project I planned to do for quite a while. This program plans on helping japanese learners on being able to copy/see meanings of kanjis they see. It allows user to easily choose an area in their screen and gives the kanjis along with their meanings in that area to the user.

This project is still in development.

# Requirements
This project requires Tesseract-OCR 5.4.0 to be in your computer. For windows download,
https://github.com/UB-Mannheim/tesseract/wiki
Make sure to download japanese language from additional languages.

For manuel, you need Python(tested with 3.12)

# Exe File
To download .exe file,
https://drive.google.com/file/d/146l5ZBrJ90TTKHxuh-PaAvX5giG0yQGS/view?usp=sharing
double click on the "main" file to start the program.

If your tesseract is not at "C:\\Program Files\\Tesseract-OCR\\tesseract.exe", program will crash. If that happens, please manually setup the program.


# Manual Setup
Step 1 - Download the open source files
Step 2 - Open ImageReader.py file
Step 3 - At line 10, change the path to where your "tesseract.exe" located at
Step 4 - Open cmd on the project directory
Step 5 - Download the required libraries(versions are given in requirements.txt), commands are given below
        pip install cx_Freeze
        pip install pillow
        pip install pyqt5
        pip install pynput
        pip install requests
        pip install pytesseract
        pip install sudachipy
        pip install sudachidict_core
Step 6 - execute "python setup.py build" command
Step 7 - Go into "build/exe.win-amd64-3.12" directory, you can open the program with main.exe file


# How to use
After completing the setup, open the main.exe file. Your screen will be layered with transparent gray color. Choose an area by clicking, dragging and releasing. After that, it will pop-up a window that gives you the image of area you choose, Kanji along with its meaning, and prev/next buttons. By clicking prev/next buttons, you can move between different kanjis in the picture. By closing the program, all processes ends.

![ss](https://github.com/furkandegirmenci/KanjiReader/assets/92688554/65342071-5653-4591-90ec-20ae195022ab) ![ss1](https://github.com/furkandegirmenci/KanjiReader/assets/92688554/f10ad04e-8dfc-4d0f-900a-1cf8a312a367)
