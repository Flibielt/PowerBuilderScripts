import codecs
import os
from shutil import copyfile

count = 0
for root, dirs, files in os.walk("folder", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        #print(fileName)
        outFile = "diff\\" + name
        if fileName.endswith(".pbd") and "EXE" not in fileName:
            os.makedirs(os.path.dirname(outFile), exist_ok=True)
            print(os.path.dirname(outFile))
            copyfile(fileName.replace("\\", "/"), outFile)
