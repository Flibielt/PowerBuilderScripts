import codecs
import os

oldFonts = {"DINPro-Medium Unicode MS", "DINPro-Medium CE", "MS Sans Serif", "Courier New CE", "Microsoft Sans Serif", "@Arial Unicode MS",
            "Arial Unicode MS", "Tahoma", "Garamond", "Courier New", "MS Serif", "Arial CE",  "Arial",  "Fixedsys"}
newFont = "DINPro-Medium"
# Webdings, Windings should be ignored

for root, dirs, files in os.walk("folderName", topdown=False):
    for name in files:
        fileName = os.path.join(root, name)
        if "svn" not in fileName:
            print(fileName)
            outFile = "folderName_out" + fileName[fileName.find("\\"):]
            os.makedirs(os.path.dirname(outFile), exist_ok=True)
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    for font in oldFonts:
                        if font.lower() in line.lower():
                            line = line.lower().replace(font.lower(), newFont)

                    with open(outFile, "a") as fOut:
                        fOut.write(line.rstrip())
                        fOut.write("\n")
