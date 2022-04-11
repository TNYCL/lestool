from os import path
import os
import ssl
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import main

zip_url = "https://cdn.tnycl.com/project_creator/template.zip"
template_exist = path.exists(os.getcwd() + "/assets/project_creator/template")

def download(extract_to='./assets/project_creator/template'):
    if template_exist == False:
        main.warn('Template folder not exist, downloading.')
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(zip_url, context=context)
            main.message('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path=extract_to)
            main.message('Template folder successfully created.')
            return True
        except:
            main.error('There was a problem downloading the settings folder.', True)
            return
    return True

