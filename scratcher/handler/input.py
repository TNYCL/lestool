from scratcher.handler import output
from scratcher.handler import check
import main

def runtask():
    project_name = input("  Project Name: ")
    author = input("  Author: ")

    check.download()
    try:
        output.duplicatefolder(project_name, author)
        main.success(f'{project_name} add-on project successfully created, path: projects/scratcher/{project_name}', True)
    except:
        main.error("Unknown error.")
        return
