import os

def openfolder(path):
    path = os.path.realpath(path)
    os.startfile(path)