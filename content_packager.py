from colorama import Fore, Back, Style
import main
import map_packer
import skin_packer

def select_content_type():
    print(Fore.LIGHTBLACK_EX + "  0. Back to main")
    print(Fore.CYAN + "  1. Skin Packager")
    print(Fore.CYAN + "  2. Map Packager")
    operation = input(Fore.RESET + "\n  Select an option: ")
    if(operation == "0"):
        main.return_main()
    elif operation == "1":
        main.clear_console()
        skin_packer.run()
    elif operation == "2":
        main.clear_console()
        map_packer.run()
    else:
        main.error("Wrong Option.\n", True)
        select_content_type()

def run():
    main.message("Content Packager\n", True)
    
    select_content_type()