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
    pname = input('Normal Name: ')
    shortedname = input('Shorted Name: ')

    if len(pname) == 0:
        input("\n\n  Press enter to return main menu.")
        main.error("Normal name cannot be left blank.", True)
        main.return_main()
        return
    if len(shortedname) == 0:
        input("\n\n  Press enter to return main menu.")
        main.error("Shorted name cannot be left blank.", True)
        main.return_main()
        return

    check.download()

    main.message('Select folder needs to be packaged. \n', True)
    filepath = fd.askdirectory(title='Select Folder')
    if filepath != '':
        main.message('Folder selected: Path => {path}'.format(path=str(filepath)))
        from ..util import file
        file.checkall()
    else:
        main.error('Folder not selected.', True)