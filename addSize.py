import codecs
import os

defaultWidth = 400
defaultHeight = 120

for root, dirs, files in os.walk("folderName", topdown=False):
    for name in files:
        fileName = os.path.join(root, name)
        outFile = "folderName_out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        button = False
        lastLine = ""
        isWidthProp = False
        isHeightProp = False
        if ".svn" not in fileName:
            print(fileName)
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    if button:
                        if "integer width" in line.lower() or "int width" in line.lower():
                            isWidthProp = True
                        elif "integer height" in line.lower() or "int height" in line.lower():
                            isHeightProp = True
                        elif "end type" in line.lower():
                            if " from u_dynamic_button within " not in lastLine.lower():
                                if not isWidthProp:
                                    with open(outFile, "a") as fOut:
                                        fOut.write("integer width = " + str(defaultWidth))
                                        fOut.write("\n")
                                if not isHeightProp:
                                    with open(outFile, "a") as fOut:
                                        fOut.write("integer height = " + str(defaultHeight))
                                        fOut.write("\n")
                            button = False
                            isWidthProp = False
                            isHeightProp = False
                    elif " from u_dynamic_button within " in line or "`cb_" in line or "`pb_" in line:
                        button = True

                    lastLine = line
                    with open(outFile, "a") as fOut:
                        fOut.write(line.rstrip())
                        fOut.write("\n")
