import os
from ..handler import create
from pathlib import Path
from ..handler import select
import main
import shutil

def openfolder(path):
    path = os.path.realpath(path)
    os.startfile(path)

def checkall():
    global directory
    directory = select.filepath + '/{}'
    REQUIRED_FOLDERS = [
        "/Skins",
        "/Skins/Slim",
        "/Skins/Slim/Free",
        "/Skins/Slim/Paid",
        "/Skins/Steve",
        "/Skins/Steve/Free",
        "/Skins/Steve/Paid",
        "/Arts"
    ]
    REQUIRED_FILES = [
        "/Arts/keyart.png",
        "/Arts/partnerart.png",
        "/Arts/thumbnail.jpg"
    ]

    for folder in REQUIRED_FOLDERS:
        if not os.path.exists(directory.format(folder)):
            main.error(f"Folder {folder} is marked as required, but does not exist.", True)
            return
    for file in REQUIRED_FILES:
        if not Path(directory.format(file)).is_file():
            main.error(f"Folder {folder} is marked as required, but does not exist.", True)
            return

    main.message('Files are verified, progressing.\n', True)
    global createdfile
    global skinfolder
    global steve
    global slim
    createdfile = create.Create()
    createdfile.copyfile()
    skinfolder = createdfile.path  + 'Content/skin_pack'
    steve = Steve()
    slim = Slim()
    main.message(f'{getskincount()} skin included. \n\n')
    create.createproject()
    main.success(f'{select.pname} project has been successfully packaged, path: projects/skin/{select.pname}')

def getskincount(): return len(steve.output) + len(slim.output)

class Slim:
    def __init__(self, names=[]):
        free = directory.format('/Skins/Slim/Free')
        paid = directory.format('/Skins/Slim/Paid')
        for name in os.listdir(free):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(free + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_customSlim.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.customSlim', realname + '_customSlim.png', 'free')
            main.message('Including (Slim -> Free): {}'.format(realname))
        
        for name in os.listdir(paid):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(paid + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_customSlim.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.customSlim', realname + '_customSlim.png', 'paid')
            main.message('Including (Slim -> Paid): {}'.format(realname))
        self.output = names

class Steve:
    def __init__(self, names=[]):
        free = directory.format('/Skins/Steve/Free')
        paid = directory.format('/Skins/Steve/Paid')
        for name in os.listdir(free):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(free + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_custom.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.custom', realname + '_custom.png', 'free')
            main.message('Including (Steve -> Free): {}'.format(realname))
        
        for name in os.listdir(paid):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(paid + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_custom.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.custom', realname + '_custom.png', 'paid')
            main.message('Including (Steve -> Paid): {}'.format(realname))
        self.output = names
            