import shutil
import tkinter as tk
from tkinter import filedialog as fd
from colorama import Fore, Back, Style
import os
import ssl
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import codecs
import json
import uuid
import main

root = tk.Tk()
root.withdraw()

def get_assets_folder():
    return os.path.join(os.getcwd(), "assets/map")

def download_assets(extract_to='./assets/map/settings'):
    settings_url = "https://cdn.tnycl.com/map_packer/settings.zip"
    template_url = "https://cdn.tnycl.com/map_packer/template.zip"

    settings_exist = os.path.exists(os.path.join(get_assets_folder(), "settings"))
    template_exist = os.path.exists(os.path.join(get_assets_folder(), "template"))

    if settings_exist == False:
        main.warn('Settings not exists, downloading.')
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(settings_url, context=context)

            main.message('Settings ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path=extract_to)
            main.message('Settings folder successfully created.', True)
        except Exception:
            main.error('There was a problem downloading the template folder.', True)
            return
    if template_exist == False:
        main.warn('Template not exists, downloading.', True)
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(template_url, context=context)
            
            main.message('Template ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path='./assets/map/template')
            main.message('Template folder successfully created.')
        except Exception:
            main.error('There was a problem downloading the settings folder.', True)
            return
    return True

def check_folders():
    REQUIRED_FOLDERS = [
     "/Arts",
     "/Arts/Ingame",
     "/Arts/Ingame/panorama.jpg",
     "/Arts/Ingame/packicon.jpg",
     "/Arts/keyart.png",
     "/Arts/thumbnail.jpg",
     "/Arts/partnerart.png",
     "/world.zip"
    ]
    for folder in REQUIRED_FOLDERS:
        if not os.path.exists(filepath + folder):
            main.error(f"Folder {folder} is marked as required, but does not exist.", True)
            return
    
    main.message('Files are verified, progressing.\n', True)
    build_project()

def build_project():
    project_path = os.getcwd() + '/projects/map/' + project_name + '/'

    try:
        shutil.copytree('assets/map/settings', project_path)
    except FileExistsError:
        os.startfile(os.path.realpath(os.getcwd() + '/projects/map/' + project_name))
        main.error('This project is already packaged.', True)
        return

    try:
        world_file = ZipFile(filepath + '/world.zip', 'r')
        world_file.extractall(path=project_path + 'Content/world_template/')
        main.message('world.zip successfully processed.')
    except Exception:
        main.error("World files couldn't be processed.", True)
        return

    worldtemplate_path = project_path + "Content/world_template/"
    with codecs.open(worldtemplate_path + "levelname.txt", 'w', 'utf-8') as file:
        file.write(project_name)
        file.close()
    
    leveldat_old = worldtemplate_path + "level.dat_old"
    world_resource_pack_history = worldtemplate_path + "world_resource_pack_history.json"
    world_behavior_pack_history = worldtemplate_path + "world_behavior_pack_history.json"
    if os.path.exists(leveldat_old):
        os.remove(leveldat_old)
    if os.path.exists(world_resource_pack_history):
        os.remove(world_resource_pack_history)
    if os.path.exists(world_behavior_pack_history):
        os.remove(world_behavior_pack_history)

    manifest = worldtemplate_path + "manifest.json"
    with open(manifest) as file:
        data = json.load(file)
        data['header']['uuid'] = str(uuid.uuid4())
        data['modules'][0]['uuid'] = str(uuid.uuid4())
        data['metadata']['authors'][0] = str(project_author)
        json.dump(data, open(manifest, 'w'), indent=4)

    with codecs.open(worldtemplate_path + "texts/en_US.lang", "a", "utf-8") as file:
        file.write("pack.name=" + project_name + "\n")
        file.write("pack.description=" + project_description)
    world_icon = worldtemplate_path + "world_icon.jpeg"
    if os.path.exists(world_icon): os.remove(world_icon)
    shutil.copy(filepath + "/arts/thumbnail.jpg", world_icon)

    #skin folder
    has_skin_pack = os.path.exists(filepath + "/skins")
    if has_skin_pack:
        try:
            shutil.copytree(filepath + '/skins', project_path + 'Content/skin_pack/', dirs_exist_ok=True)
            main.message('Skin files successfully processed.')
        except Exception as ex:
            main.error(ex, True)
            return
    
    has_addons = os.path.exists(filepath + "/addons")
    if has_addons:
        BP = os.path.exists(filepath +  "/addons/BP")
        RP = os.path.exists(filepath +  "/addons/RP")
        if BP:
            try:
                new_path = worldtemplate_path + "behavior_packs/" + shorted_project_name + "_BP"
                shutil.copytree(filepath + "/addons/BP", new_path, dirs_exist_ok=True)

                global bp_uuid
                bp_uuid = ""
                with open(new_path + "/manifest.json") as file:
                    data = json.load(file)
                    bp_uuid = data['header']['uuid']
                with open(worldtemplate_path + "world_behavior_packs.json") as file:
                    data = json.load(file)
                    data[0]['pack_id'] = str(bp_uuid)
                    json.dump(data, open(worldtemplate_path + "world_behavior_packs.json", 'w'), indent=4)
                
                main.message('Add-on:BP successfully processed.')
            except Exception:
                main.error("Add-on:BP files couldn't be processed.", True)
                return
        else:
            world_behavior_pack = worldtemplate_path + "world_behavior_packs.json"
            if os.path.exists(world_behavior_pack):
                os.remove(world_behavior_pack)
        
        if RP:
            try:
                new_path = worldtemplate_path + "resource_packs/" + shorted_project_name + "_RP"
                shutil.copytree(filepath + "/addons/RP", new_path, dirs_exist_ok=True)

                global rp_uuid
                rp_uuid = ""
                with open(new_path + "/manifest.json") as file:
                    data = json.load(file)
                    bp_uuid = data['header']['uuid']
                with open(worldtemplate_path + "world_resource_packs.json") as file:
                    data = json.load(file)
                    data[0]['pack_id'] = str(bp_uuid)
                    json.dump(data, open(worldtemplate_path + "world_resource_packs.json", 'w'), indent=4)

                main.message('Add-on:RP successfully processed.')
            except Exception:
                main.error("Add-on:RP files couldn't be processed.", True)
                return
        else:
            world_resource_pack = worldtemplate_path + "world_resource_packs.json"
            if os.path.exists(world_resource_pack):
                os.remove(world_resource_pack)
        main.message("Add-on files are successfully processed.")
    
    photo_count = 0
    marketingart_path = project_path + "Marketing Art/"
    for file in os.listdir(filepath + '/arts/ingame'):
        if file == "packicon.jpg": continue
        if file == "panorama.jpg": continue
        shutil.copy(filepath + "/arts/ingame/" + file, marketingart_path + project_name + "_MarketingScreenshot_" + str(photo_count) + ".jpg")
        photo_count+=1
    shutil.copy(filepath + "/arts/keyart.png", marketingart_path + project_name + "_MarketingKeyArt.png")
    shutil.copy(filepath + "/arts/partnerart.png", marketingart_path + project_name + "_MarketingPartnerArt.png")

    photo_count = 0
    storeart_path = project_path + "Store Art/"
    for file in os.listdir(filepath + '/arts/ingame'):
        if file == "packicon.jpg":
            shutil.copy(filepath + "/arts/ingame/" + file, storeart_path + project_name + "_packicon_0.jpg")
            continue
        if file == "panorama.jpg":
            shutil.copy(filepath + "/arts/ingame/" + file, storeart_path + project_name + "_panorama_0.jpg")
            continue
        shutil.copy(filepath + "/arts/ingame/" + file, storeart_path + project_name + "_MarketingScreenshot_" + str(photo_count) + ".jpg")
        photo_count+=1
    shutil.copy(filepath + "/arts/thumbnail.jpg", storeart_path + project_name + "_Thumbnail_0.jpg")
    print("\n")
    main.success(f'{project_name} project has been successfully packaged, path: projects/map/{project_name}')

def select_file():
    if(download_assets()):
        main.message('Select folder needs to be packaged. \n', True)
        global filepath
        filepath = fd.askdirectory(title='Select Folder')
        if filepath != '':
            main.message(f'Folder selected: {str(filepath)}\n', True)
            check_folders()
        else:
            main.error('Folder not selected.', True)

def run():
    main.message("Map Packager\n")

    global project_name
    global shorted_project_name
    global project_description
    global project_author

    try:
        project_name = input('  Normal Name'+Fore.RESET+': ')
        if len(project_name) == 0:
            main.error("Normal name cannot be left blank.")
            input("\n\n  Press enter to return main menu.")
            main.return_main()
            return

        shorted_project_name = input('  Shorted Name'+Fore.RESET+': ')
        if len(shorted_project_name) == 0:
            main.error("Shorted name cannot be left blank.")
            input("\n\n  Press enter to return main menu.")
            main.return_main()
            return

        project_description = input('  Description'+Fore.RESET+': ')
        if len(project_description) == 0:
            main.error("Description cannot be left blank.")
            input("\n\n  Press enter to return main menu.")
            main.return_main()
            return

        project_author = input('  Author'+Fore.RESET+': ')
        if len(project_author) == 0:
            main.error("Author cannot be left blank.")
            input("\n\n  Press enter to return main menu.")
            main.return_main()
            return

        project_name.replace(" ", "")
        select_file()
    except:
        input("\n\n  Press enter to continue.")
        main.clear_console()
        main.message("Returned to main menu. \n")
        main.main()
        return
    
    input("\n\n  Press enter to return main menu.")
    main.return_main()