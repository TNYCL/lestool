from os import path
import os
import ssl
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import main

settings_url = "https://cdn.tnycl.com/skin_packer/settings.zip"
template_url = "https://cdn.tnycl.com/skin_packer/template.zip"
settings_exist = path.exists(os.getcwd() + "/assets/skin/settings")
template_exist = path.exists(os.getcwd() + "/assets/skin/template")

def download(extract_to='./assets/skin/settings'):
    if settings_exist == False:
        main.message('Settings folder not exists, downloading.')
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(settings_url, context=context)
            main.message('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path=extract_to)
            main.message('Settings folder successfully created.\n')
        except Exception:
            main.error('There was a problem downloading the template.zip')
    if template_exist == False:
        main.message('Template folder not exists, downloading.')
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(template_url, context=context)
            main.message('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path='./assets/skin/template')
            main.message('Template folder successfully created.\n')
        except Exception:
            main.error('There was a problem downloading the settings.zip')
    return True

