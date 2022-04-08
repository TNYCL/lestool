from skin.handler import select
import main

def run():
    print("Skin Packager\n")

    try:
        select.opendialog()
    except:
        input("\n\n  Press enter to continue.")
        main.clear_console()
        main.message("Returned to main menu. \n")
        main.main()
        return

    input("\n\n  Press enter to return main menu.")
    main.return_main()
