#pip install pyautogui
#pip install pynput

import pyautogui
import tkinter as tk
from PIL import ImageGrab
from tkinter import messagebox
from pynput import mouse
from PIL import Image
import Ui




def takePicture():
    with mouse.Listener(on_click=on_click) as listener:
        Ui.screenLayer()
        listener.join()


    img = Image.open('screenshot.png')
    return img

def on_click(x, y, button, pressed):
    global x1, x2, y1, y2

    if pressed:
        print(f"Mouse button {button} pressed at ({x}, {y})")
        x1, y1 = x, y
    else:
        print(f"Mouse button {button} released at ({x}, {y})")
        x2, y2 = x, y
        if(x1 > x2):
            temp = x1
            x1 = x2
            x2 = temp
        if(y1 > y2):
            temp = y1
            y1 = y2
            y2 = temp
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        screenshot.save('screenshot.png')
        return False