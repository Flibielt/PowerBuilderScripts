import os

currentDirectory = os.getcwd()

dirs = os.listdir(currentDirectory)

for item in dirs:
    if item.endswith(".srd") or item.endswith(".srf") or item.endswith(".sru") or item.endswith(".srw") or item.endswith(".srs") or item.endswith(".srm") or item.endswith(".srq"):
        os.remove(os.path.join(currentDirectory, item))