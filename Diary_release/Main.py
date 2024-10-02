import time
from threading import Thread
import keyboard
import pyautogui
from Main_window import main_window
from Weekly_window import weekly_window
import Settings

def func():

    global start_thread

    while True:
        if start_thread:
            time.sleep(0.3)
            pyautogui.moveTo(int(1920 / 2), int(1080 / 2 - 100))
            pyautogui.click()
            keyboard.press('win')
            keyboard.press('shift')
            keyboard.press('left')
            keyboard.release('win')
            keyboard.release('shift')
            keyboard.release('left')
            start_thread = False
        else:
            time.sleep(0.5)

Settings.init()

start_thread = False

th = Thread(target=func, daemon=True)
th.start()

while True:
    if Settings.flag_for_windows == 1:
        start_thread = True
        main_window()
    elif Settings.flag_for_windows == 2:
        weekly_window()
    elif Settings.flag_for_windows == 3:
        weekly_window()
    