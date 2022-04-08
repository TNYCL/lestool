import tkinter as tk
from tkinter import filedialog as fd
from colorama import Fore, Back, Style
import shutil
import os
import main

root = tk.Tk()
root.withdraw()

VERSION = "0.1"
DEBUG = True

def select_file():
    main.message('Select folder needs to be commented.\n')
    global filepath
    filepath = fd.askdirectory(title='Select Folder')
    if filepath != '':
        main.message(f'Folder selected: Path => {str(filepath)}')
        build_project()
    else:
        main.error('Folder not selected.', clear=False)


def build_project():
    shutil.copy()

def run():
    main.message("Addon Commentor\n")

    try:
        select_file()
    except:
        input("\n\n  Press enter to continue.")
        main.clear_console()
        main.message("Returned to main menu \n")
        main.main()
        return

    input("\n\n  Press enter to return main menu.")
    main.message("Returned to main menu \n", True)
    main.main()