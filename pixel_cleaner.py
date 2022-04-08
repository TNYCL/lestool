import tkinter as tk
from tkinter import filedialog as fd
from colorama import Fore, Back, Style
import os
import main
import cv2

root = tk.Tk()
root.withdraw()

def select_file():
    main.message('Select skin file needs to be clear.', True)
    global filepath
    filepath = fd.askopenfilenames(parent=root, title='Select Skin File', filetypes=[('Image Files', '.png'), ('Image Files', '.jpg')])
    if filepath != '':
        main.message(f'Files selected: Path => {filepath}')
    else:
        main.error('File not selected.', True)

def select_resolution():
    print(Fore.LIGHTBLACK_EX + "  0. Back to main")
    print(Fore.CYAN + "  1. 64x64")
    print(Fore.CYAN + "  2. 128x128")
    operation = input(Fore.RESET + "\n  Select an option: ")
    if(operation == "0"):
        main.message("Returned to main menu \n", True)
        main.main()
    elif operation == "1":
        select_file()
        res_64x64()
    elif operation == "2":
        select_file()
        res_128x128()
    else:
        main.error("Wrong Option.\n")
        select_resolution()

def res_64x64():
    for file in filepath:
        try:
            skin = cv2.imread(file, cv2.IMREAD_UNCHANGED)

            name = os.path.basename(file)
            if name.endswith(".png"): name = name.replace(".png", "")
            else: name = name.replace(".jpg", "")

            skin[0:8, 0:8, 3] = 0
            skin[0:8, 0:8, 3] = 0
            skin[0:8, 24:40, 3] = 0
            skin[0:8, 56:64, 3] = 0
            skin[16:20, 0:4, 3] = 0
            skin[16:20, 12:20, 3] = 0
            skin[16:20, 36:44, 3] = 0
            skin[16:20, 50:64, 3] = 0
            skin[20:48, 54:64, 3] = 0
            skin[32:36, 50:54, 3] = 0
            skin[48:52, 58:64, 3] = 0
            skin[52:64, 62:64, 3] = 0
            skin[32:36, 0:4, 3] = 0
            skin[32:36, 12:20, 3] = 0
            skin[32:36, 36:44, 3] = 0
            skin[48:52, 0:4, 3] = 0
            skin[48:52, 12:20, 3] = 0
            skin[48:52, 28:36, 3] = 0
            skin[48:52, 42:52, 3] = 0
            skin[52:64, 46:48, 3] = 0

            cv2.imwrite(file.replace(name, name + "_cleared"), skin)
        except Exception as ex:
            print(ex)

def res_128x128():
    for file in filepath:
        skin = cv2.imread(file, cv2.IMREAD_COLOR)

        skin[0:16, 0:16] = (255, 0, 0)

        #cv2.imwrite(filepath, skin)
        print(str(os.path.basename(file)))

def run():
    main.message("Pixel Cleaner\n", True)
    
    try:
        select_resolution()
    except:
        input("\n\n  Press enter to continue.")
        main.clear_console()
        main.message("Returned to main menu. \n")
        main.main()
        return

    input("\n\n  Press enter to return main menu.")
    main.return_main()