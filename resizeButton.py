import codecs
import os

defaultWidth = 539
defaultHeight = 100

for root, dirs, files in os.walk("proba", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "proba_out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        isWidth = False
        isHeight = False
        lastLine = ""
        if name.startswith("w_") or name.startswith("uov_") or name.startswith("u_"):
            button = False
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    if "from u_dynamic_button" in line:
                        button = True
                    elif "type cb_" in line or "type pb_" in line:
                        if "`cb_" in line or "`pb_" in line:
                            button = True
                    elif "end type" in line:
                        if "from u_dynamic_button" not in lastLine and button:
                            if not isWidth:
                                with open(outFile, "a") as fOut:
                                    fOut.write("integer width = " + str(defaultWidth))
                                    fOut.write("\n")
                            if not isHeight:
                                with open(outFile, "a") as fOut:
                                    fOut.write("integer height = " + str(defaultHeight))
                                    fOut.write("\n")
                        button = False
                        isWidth = False
                        isHeight = False
                    
                    if button:
                        if "integer width" in line.lower() or "int width" in line.lower():
                            isWidth = True
                            width = line[line.find("=") + 1:]
                            if int(width.strip()) > 90:
                                line = line[:line.find("=")] + "= " + str(defaultWidth)
                        elif "integer height" in line.lower() or "int height" in line.lower():
                            isHeight = True
                            height = line[line.find("=") + 1:]
                            if int(height.strip()) > 90:
                                line = line[:line.find("=")] + "= " + str(defaultHeight)
                    
                    with open(outFile, "a") as fOut:
                        fOut.write(line.rstrip())
                        fOut.write("\n")
                    
                    lastLine = line
