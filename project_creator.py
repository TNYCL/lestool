from scratcher.handler import input as inp
import main

def run():
    main.message("Add-on Project Creator\n")

    try:
        inp.runtask()
    except:
        input("\n\n  Press enter to continue.")
        main.clear_console()
        main.message("Returned to main menu. \n")
        main.main()
        return

    input("\n\n  Press enter to return main menu.")
    main.return_main()
