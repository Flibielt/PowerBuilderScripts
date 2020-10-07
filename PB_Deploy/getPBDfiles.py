import codecs
import os
from shutil import copyfile

def getPBDFiles(projectFolder):

    projectFolder = projectFolder.replace("\\", "/")

    for root, dirs, files in os.walk(projectFolder + "/EXE", topdown=False):
        for name in files:
            if name.endswith(".pbd"):
                fileName = os.path.join(root, name)
                print(fileName)
                os.remove(fileName)

    for root, dirs, files in os.walk(projectFolder, topdown=False):
        for name in files:
            fileName = os.path.join(root, name)
            
            outFile = projectFolder + "/EXE/" + name
            if fileName.endswith(".pbd") and "EXE" not in fileName:
                print(fileName)
                copyfile(fileName, outFile)
