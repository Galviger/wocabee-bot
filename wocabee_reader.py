from logging.config import listen
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 100)
canvas1.pack()
label1 = tk.Label(root, text = "Tohle bohužel nedám, sorka.")

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def pickOne():
    click(710, 200)
    if pyautogui.pixel(1150, 540)[0] > 200:
        click(1150, 540)
    elif pyautogui.pixel(1150, 610)[0] > 200:
        click(1150, 540)
    elif pyautogui.pixel(1150, 670)[0] > 200:
        click(1150, 540)
    time.sleep(10)

def pairs():
    click(710, 200)
    if pyautogui.pixel(1100, 400)[0] > 200:
        click(1100, 400)
    elif pyautogui.pixel(1100, 460)[0] > 200:
        click(1100, 460)
    elif pyautogui.pixel(1100, 540)[0] > 200:
        click(1100, 540)
    elif pyautogui.pixel(1100, 620)[0] > 200:
        click(1100, 620)
    elif pyautogui.pixel(1100, 700)[0] > 200:
        click(1100, 700)
    elif pyautogui.pixel(1100, 770)[0] > 200:
        click(1100, 770)
    time.sleep(10)

def completeWord():
    canvas1.create_window(100, 50, window=label1)

def listenAndWrite():
    click(710, 200)
    time.sleep(0.5)
    click(1100, 670)
    time.sleep(10)

def translate():
    click(710, 200)
    time.sleep(0.5)
    click(1100, 610)
    time.sleep(10)

def pictureReader():
    click(710, 200)
    time.sleep(0.5)
    click(1100, 760)
    time.sleep(10)

def picturePicker():
    canvas1.create_window(100, 50, window=label1)

while keyboard.is_pressed('q') == False:
    while pyautogui.pixel(1400, 270)[0]>100:
        if pyautogui.pixel(1100, 400)[0] == 40 and pyautogui.pixel(1100, 610)[0] == 0 and pyautogui.pixel(1100, 670)[0] == 0:
            pickOne()
        elif pyautogui.pixel(1100, 400)[0] == 40 and pyautogui.pixel(1100, 460)[0] == 40 and pyautogui.pixel(1100, 540)[0] == 40 and pyautogui.pixel(1100, 620)[0] == 0 and pyautogui.pixel(1100, 700)[0] == 0 and pyautogui.pixel(1100, 770)[0] == 0:
            pairs()
        elif pyautogui.pixel(940, 440)[0] == 255 and pyautogui.pixel(1100, 520)[0] == 255 and pyautogui.pixel(1100, 750)[0] == 19:
            listenAndWrite()
        elif pyautogui.pixel(1100, 400)[0] == 40 and pyautogui.pixel(940, 450)[0] == 255 and pyautogui.pixel(1100, 530)[0] == 255:
            translate()
        elif pyautogui.pixel(1100, 690)[0] == 255 and pyautogui.pixel(1100, 760)[0] == 2:
            pictureReader()
        elif pyautogui.pixel(1100, 540)[0] == 255 and pyautogui.pixel(1100, 740)[0] == 19:
            completeWord()
root.mainloop()
