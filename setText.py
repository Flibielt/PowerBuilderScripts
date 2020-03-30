import codecs
import os

for root, dirs, files in os.walk("folderName", topdown=False):
    for name in files:
        fileName = os.path.join(root, name)
        if "svn" not in fileName:
            print(fileName)
            outFile = "folderName_out" + fileName[fileName.find("\\"):]
            os.makedirs(os.path.dirname(outFile), exist_ok=True)
            with codecs.open(fileName, encoding='cp1250') as f:
                for line in f:
                    if "cb_" in line or "pb_" in line.lower():
                        if ".text" in line.lower() and ".textsize" not in line.lower():
                            if line.lower().find(".text") > line.find("="):
                                line = line[:line.lower().find(".text")] + ".get_text()"
                            else:
                                line = line.replace("=", "")
                                line = line[:line.lower().find(".text")] + ".set_text(" + line[line.lower().find(
                                    ".text"):] + ")"
                                while "( " in line:
                                    line = line.replace("( ", "(")
                                while " )" in line:
                                    line = line.replace(" )", ")")
