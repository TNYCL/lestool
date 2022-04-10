from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import requests
import main
import ssl
import json
import os

VERSION = ""
LAST_UPDATE = ""

def get_version():
    sent = {"security_hash": main.SECURITY_HASH}
    response = requests.post(url="https://api.tnycl.com/lespacker/version.php", params=sent)
    incoming = json.loads(response.text)

    global VERSION
    VERSION = incoming['version']
    global LAST_UPDATE
    LAST_UPDATE = incoming['last_update']

def check_update():
    get_version()
    if VERSION == main.VERSION: return
    
    main.warn(f"New update founded v{VERSION}")
    download_update()
    return True

def download_update(extract_to='./'):
    settings_url = "https://api.tnycl.com/lespacker/update.zip"
    try:
        context = ssl._create_unverified_context()
        http_response = urlopen(settings_url, context=context)
        main.message(f'v{VERSION} files downloading...')

        zipfile = ZipFile(BytesIO(http_response.read()))
        zipfile.extractall(path=extract_to)
        main.message(f'v{VERSION} files extracting.')

        main.clear_console()
        main.success(f'{main.NAME} successfully updated to v{VERSION}, open new file: "tool.v{VERSION}.exe".', True)
        main.exit_program(False)
    except Exception:
        main.error('There was a problem downloading process.', True)
        return False