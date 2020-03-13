import codecs
import os

oldFonts = {"MS Sans Serif", "Courier New CE", "Arial CE", "Arial", "Microsoft Sans Serif", "@Arial Unicode MS", "Arial Unicode MS", "Tahoma", "Garamond", "Courier New"}
newFont = "DINPro-Medium"
# Webdings, Windings, Fixedsys  ??

for root, dirs, files in os.walk("folderName", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "folderName_out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                print(line)