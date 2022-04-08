import tkinter as tk
from tkinter import filedialog as fd
from colorama import Fore, Back, Style
import os
import main
import cv2

root = tk.Tk()
root.withdraw()

def select_file():
    main.message('Select skin files needs to be clear.', True)
    global filepath
    filepath = fd.askopenfilenames(parent=root, title='Select Skin File', filetypes=[('Image Files', '.png'), ('Image Files', '.jpg')])
    if filepath != '':
        main.message(f'Files selected: Path => {filepath}')
        main.clear_console()
    else:
        main.error('File not selected.', True)

def select_resolution():
    """print(Fore.LIGHTBLACK_EX + "  0. Back to main")
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
        select_resolution()"""
    select_file()
    for file in filepath:
        try:
            skin = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            width, height, channels = skin.shape

            name = os.path.basename(file)
            if name.endswith(".png"): name = name.replace(".png", "")
            else: name = name.replace(".jpg", "")

            if width and height == 128:
                res_128x128(skin, file, name)
            elif width and height == 64:
                res_64x64(skin, file, name)
            else: main.error(f"{width}x{height} ({name}): Wrong skin resolution.", False)
        except Exception as ex:
            main.error(ex)


def res_64x64(skin, file, name):
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
    main.message(f"64x64: {name} successfully cleared.")

def res_128x128(skin, file, name):
    skin[0:16, 0:16, 3] = 0
    skin[0:16, 48:80, 3] = 0
    skin[0:16, 112:128, 3] = 0
    skin[32:40, 0:8, 3] = 0
    skin[32:40, 24:40, 3] = 0
    skin[32:40, 72:88, 3] = 0
    skin[32:40, 100:128, 3] = 0
    skin[40:96, 108:128, 3] = 0
    skin[64:72, 100:108, 3] = 0
    skin[96:104, 116:128, 3] = 0
    skin[104:128, 124:128, 3] = 0
    skin[64:72, 0:8, 3] = 0
    skin[64:72, 24:40, 3] = 0
    skin[64:72, 72:88, 3] = 0
    skin[96:104, 0:8, 3] = 0
    skin[96:104, 24:40, 3] = 0
    skin[96:104, 56:72, 3] = 0
    skin[96:104, 84:104, 3] = 0
    skin[104:128, 92:96, 3] = 0
    
    cv2.imwrite(file.replace(name, name + "_cleared"), skin)
    main.message(f"128x128: {name} successfully cleared.")

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