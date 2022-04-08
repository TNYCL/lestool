from skin.handler import select
import sys
import main
from colorama import Fore, Back, Style

def run():
    print("Skin Packager\n")

    try:
        select.opendialog()
    except:
        input("\n\n  Press enter to continue.")
        main.clear_console()
        main.message("Returned to main menu \n")
        main.main()
        return

    input("\n\n  Press enter to return main menu")
    main.message("Returned to main menu \n", True)
    main.main()