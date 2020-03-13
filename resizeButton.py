import codecs
import os

defaultWidth = 539
defaultHeight = 100

for root, dirs, files in os.walk("folderName", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "folderName_out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        if name.startswith("w_") or name.startswith("uov_") or name.startswith("u_"):
            button = False
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    if "from u_dynamic_button" in line:
                        button = True
                    elif "end type" in line:
                        button = False
                    
                    if button:
                        if "integer width" in line.lower() or "int width" in line.lower():
                            line = line[:line.find("=")] + " " + str(defaultWidth)
                        elif "integer height" in line.lower() or "int height" in line.lower():
                            line = line[:line.find("=")] + " " + str(defaultHeight)
                    
                    with open(outFile, "a") as fOut:
                        fOut.write(line.rstrip())
                        fOut.write("\n")

