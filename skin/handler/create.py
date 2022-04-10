import os
import json
from ..util import uuid
from ..util import file
from ..handler import select
import codecs
import shutil
import main

pname = select.pname
shortedname = select.shortedname
src = 'assets/skin/settings'

class Create:
    def __init__(self):
        self.path = os.getcwd() + '/projects/skin/' + pname + '/'

    def copyfile(self):
        try:
            shutil.copytree(src, self.path)
        except FileExistsError:
            file.openfolder(self.path)
            main.error('This project is already packaged.', True)

selectedpath = select.filepath
createdpath = Create().path
skinpath = createdpath + 'Content/skin_pack/'
marketingartpath = createdpath + 'Marketing Art/'
storeartpath = createdpath + 'Store Art/'

def createproject():
    manifest()
    copy_art()
    text_pname()

def manifest():
    try:
        manifest = createdpath + 'Content/skin_pack/manifest.json'
        with open(manifest) as file:
            data = json.load(file)
            data['header']['name'] = f"pack.{shortedname}"
            data['header']['uuid'] = str(uuid.header)
            data['modules'][0]['uuid'] = str(uuid.modules)
            json.dump(data, open(manifest, 'w'), indent=4)
    except:
        main.error("manifest.json files couldn't be processed.")
    try: 
        skins = createdpath + 'Content/skin_pack/skins.json'
        with open(skins) as file:
            data = json.load(file)
            data['serialize_name'] = shortedname
            data['localization_name'] = shortedname
            json.dump(data, open(skins, 'w'), indent=4)
    except:
        main.error("skins.json files couldn't be processed.")

def copy_art():
    shutil.copy(selectedpath + '/Arts/keyart.png', marketingartpath + shortedname +'_MarketingKeyArt.png')
    shutil.copy(selectedpath + '/Arts/partnerart.png', marketingartpath + shortedname + '_PartnerArt.png')
    shutil.copy(selectedpath + '/Arts/thumbnail.jpg', storeartpath + shortedname + '_Thumbnail_0.jpg')

def text_pname():
    try:
        text = skinpath + 'texts/en_US.lang'
        with codecs.open(text, 'a', 'utf-8') as file:
            data = file
            data.write('skinpack.'+shortedname+'={}\n'.format(pname))
            data.close()
    except:
        main.error("texts/en_US.lang(Project Name) couldn't be processed.")

def text_skin(name):
    try:
        text = skinpath + 'texts/en_US.lang'
        with codecs.open(text, 'a', 'utf-8') as file:
            data = file
            data.write('skin.'+shortedname+'.{}={}\n'.format(name, name))
            data.close()
    except:
        main.error("texts/en_US.lang(Skin) couldn't be processed.")

def jsonparse_skin(name, geometry, texture, type):
    try:
        manifest = createdpath + 'Content/skin_pack/skins.json'
        with open(manifest) as file:
            data = json.load(file)
            data['skins'].append({"localization_name": name, "geometry": geometry, "texture": texture, "type": type})
            json.dump(data, open(manifest, 'w'), indent=4)
    except:
        main.error("skins.json couldn't be processed.")
