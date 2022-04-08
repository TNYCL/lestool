from colorama import Fore, Back, Style
import subprocess
import os
import json
import sys
import platform
import requests
import calendar
import time
import commentor
import pixel_cleaner
import update
import content_packager


NAME = "LES:Tool"
VERSION = "1.0.0"
DEBUG = True
SECURITY_HASH = "C7E876AD26C4BBF271A22CF89E94D3D2A01B4C31CE91E08E894CFCA83C1F4D5DE35512F7202A8AA16EBF0FB8D6B360B55AC23C3A67D9B0516C8AA18047BC990D"
TOKEN_VALIDATED = False

settings_path = "settings.json"
validate_url = "https://api.tnycl.com/lespacker/validate.php"

def success(message):
    print(f"{Fore.BLACK + Back.GREEN}SUCCESS:" + Style.RESET_ALL + " " + message + Fore.RESET)

def warning(message, clear=False):
    if clear: clear_console()
    print(f"{Fore.YELLOW}WARNING:" + Style.RESET_ALL + " " + message + Fore.RESET)

def warn(message, clear=False):
    if clear: clear_console()
    print(f"{Fore.YELLOW}+:" + Style.RESET_ALL + " " + message + Fore.RESET)

def err(message):
    print(f"{Fore.RED}+:" + Style.RESET_ALL + " " + message + Fore.RESET)

def error(message, clear=True):
    if clear: clear_console()
    print(f"{Back.RED + Fore.BLACK}ERROR:" +
          Fore.RED + Back.RESET + " " + message + Fore.RESET)

def message(message, clear=False):
    if clear: clear_console()
    print(f"{Fore.LIGHTCYAN_EX}-> " + Fore.RESET + message)

def main():
    print(Fore.LIGHTBLACK_EX + "  0. Exit")
    print(Fore.CYAN + "  1. Content Packager")
    print(Fore.CYAN + "  2. Addon Commentor")
    print(Fore.CYAN + "  3. Pixel Cleaner")
    operation = input(Fore.RESET + "\n  Select an option: ")

    if(operation == "0"):
        message("Good bye", True)
        input("\n Press enter to exit.")
    elif operation == "1":
        clear_console()
        content_packager.run()
    elif operation == "2":
        clear_console()
        commentor.run()
    elif operation == "3":
        clear_console()
        pixel_cleaner.run()
    else:
        error("Wrong Option.\n")
        main()

def get_hwid():
    if platform.system() == "Windows": return str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    else: 
        cmd = "system_profiler SPHardwareDataType | awk '/Serial Number/ {print $4}'"
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)
        return result.stdout.strip()

def save_token(token):
    with open(settings_path, "w+") as file:
        file.write('{"token": "'+token+'"}')

def get_token():
    if not os.path.exists(settings_path): return None
    with open(settings_path, 'r') as file:
        return json.load(file)['token']

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    print()

def validate_token(token):
    sent = {"token": token, "security_hash": SECURITY_HASH, "hwid": get_hwid(), "timestamp": calendar.timegm(time.gmtime())}
    response = requests.post(url=validate_url, params=sent)
    incoming = json.loads(response.text)

    global TOKEN_VALIDATED
    TOKEN_VALIDATED = incoming['status']

    if incoming['error'] == 2 and TOKEN_VALIDATED:
        error(incoming['message'], True)
        input("\n Press enter to exit.")

    if incoming['error'] == 3 and TOKEN_VALIDATED:
        error(incoming['message'], True)
        input("\n Press enter to exit.")

    if TOKEN_VALIDATED: 
        save_token(token)
        message(incoming['message'] + "\n")
    else:
        error(incoming['message'], True)
        input("\n Press enter to exit.")

def set_title(title):
    os.system(title)

if __name__ == "__main__":
    if not DEBUG: message(f"Welcome {NAME} Version:{VERSION}\n")
    else: 
        message(f"(Dev) {NAME} Version: {VERSION}")
        message(f"Secure Hash: {SECURITY_HASH}\n")

    update.check_update()

    if get_token() == None:
        token = input("\nEnter your token: ")
        validate_token(token)
    else:
        validate_token(get_token())

    if TOKEN_VALIDATED: main()