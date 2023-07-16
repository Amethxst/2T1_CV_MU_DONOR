import cv2
import os
import sys
import pyautogui
import numpy as np
import time
import json 
import keys
from keys import PressKey, ReleaseKey, num2, num0, num5, num8, esc


# FIND IMG FROM EXE / SCRIPT
def get_image_paths_file_path():
    if getattr(sys, 'frozen', False):
        # exe
        return os.path.join(os.path.dirname(sys.executable), 'image_paths.json')
    else:
        # script Python
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image_paths.json')


def search_images():
    img1_path, img2_path = read_image_paths()
    reference_image1 = cv2.imread(img1_path)
    reference_image2 = cv2.imread(img2_path)

    while True:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result1 = cv2.matchTemplate(screenshot, reference_image1, cv2.TM_CCOEFF_NORMED)
        result2 = cv2.matchTemplate(screenshot, reference_image2, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8

        locations1 = np.where(result1 >= threshold)
        locations2 = np.where(result2 >= threshold)

        if locations1[0].size > 0:
            macro1()  # Run macro for first img (1.png)
        elif locations2[0].size > 0:
            macro2()  # Run macro for second img (2.png)
        else:
            print("Immagine non trovata. Riprova tra 5 secondi.")
            time.sleep(5)

# "Special Cargo" -> start loop
def macro1():
    PressKey(num8)
    time.sleep(0.5)
    ReleaseKey(num8)
    time.sleep(0.5)
    
    PressKey(num5)
    time.sleep(0.5)
    ReleaseKey(num5)
    time.sleep(0.5)

    PressKey(num8)
    time.sleep(0.5)
    ReleaseKey(num8)
    time.sleep(0.5)

    PressKey(num8)
    time.sleep(0.5)
    ReleaseKey(num8)
    time.sleep(0.5)

    PressKey(num8)
    time.sleep(0.5)
    ReleaseKey(num8)
    time.sleep(0.5)

    PressKey(num5)
    time.sleep(0.5)
    ReleaseKey(num5)
    time.sleep(0.5)

# Restock Werehouse / start loop again
def macro2():
    PressKey(num5)
    time.sleep(0.5)
    ReleaseKey(num5)
    time.sleep(0.5)

    PressKey(esc)
    time.sleep(0.5)
    ReleaseKey(esc)
    time.sleep(0.5)

    PressKey(esc)
    time.sleep(0.5)
    ReleaseKey(esc)
    time.sleep(0.5)

    PressKey(num8)
    time.sleep(0.5)
    ReleaseKey(num8)
    time.sleep(0.5)

    PressKey(num8)
    time.sleep(0.5)
    ReleaseKey(num8)
    time.sleep(0.5)

    PressKey(num5)
    time.sleep(0.5)
    ReleaseKey(num5)
    time.sleep(0.5)

    time.sleep(7)   # WAIT FOR RESTOCK // EDIT IF TAKE A LOT OF TIME (7 = 7sec)

    PressKey(num5)
    time.sleep(0.5)
    ReleaseKey(num5)
    time.sleep(0.5)

    PressKey(num2)
    time.sleep(0.5)
    ReleaseKey(num2)
    time.sleep(0.5)

    PressKey(num2)
    time.sleep(0.5)
    ReleaseKey(num2)
    time.sleep(0.5)

    PressKey(num5)
    time.sleep(0.5)
    ReleaseKey(num5)
    time.sleep(0.5)

# read img paths from .json file
def read_image_paths():
    file_path = get_image_paths_file_path()

    with open(file_path) as f:
        config = json.load(f)

    img1_path = config["image1_path"]
    img2_path = config["image2_path"]

    return img1_path, img2_path




if __name__ == "__main__":
    stop_key = "q"  # stop script //idk not work :( \\
    running = True

    while running:
        search_images()  # find img

        
        if pyautogui.press(stop_key):
            running = False