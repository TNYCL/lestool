from os import path
import os
import ssl
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import main

settings_url = "https://cdn.tnycl.com/skin_packer/settings.zip"
template_url = "https://cdn.tnycl.com/skin_packer/template.zip"

def download(extract_to='./assets/skin/settings'):
    settings_exist = path.exists(os.getcwd() + "/assets/skin/settings")
    template_exist = path.exists(os.getcwd() + "/assets/skin/template")
    if settings_exist == False:
        print(os.getcwd() + "/assets/skin/settings")
        main.warn('Settings folder not exists, downloading.', True)
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(settings_url, context=context)
            main.message('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path=extract_to)
            main.message('Settings folder successfully created.\n', True)
        except Exception:
            main.error('There was a problem downloading the template.zip')
    if template_exist == False:
        print(os.getcwd() + "/assets/skin/template")
        main.warn('Template folder not exists, downloading.', True)
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(template_url, context=context)
            main.message('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path='./assets/skin/template')
            main.message('Template folder successfully created.\n', True)
        except Exception:
            main.error('There was a problem downloading the settings.zip')
    return True

