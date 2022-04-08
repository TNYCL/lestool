import tkinter as tk
from ..handler import check
from tkinter import filedialog as fd
import main
from colorama import Fore, Back, Style

root = tk.Tk()
root.withdraw()

def opendialog():
    global filepath
    global pname
    global shortedname
    
    pname = input('Project Name: ')
    shortedname = input('Shorted Name: ')

    check.download()

    filepath = fd.askdirectory(title='Select Skin Pack')
    print("")
    main.message('Checking folders...')

    from ..util import file
    file.checkall()