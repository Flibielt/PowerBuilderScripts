import codecs
import os

typeDeclaration = False
endType = False
widthProp = False
heightProp = False
typeDef = False
typeName = ""

for root, dirs, files in os.walk("..\\mc2svn17UD", topdown=False):
   for name in files:
      if name.startswith("w_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if line.strip().startswith("type"):
                    typeDeclaration = True
                    typeDef = True
                    typeName = line.strip()
                elif typeDeclaration:
                    if "end type" in line:
                        typeDeclaration = False
                        endType = True
                    elif "width" in line.lower():
                        widthProp = True
                    elif "height" in line.lower():
                        heightProp = True
                    else:
                        typeDef = False
                with open(outFile, "a") as f:
                    if "cb_" in typeName and endType and not typeDef:
                        if widthProp == False:
                            f.write("integer width = 347\n")
                        if heightProp == False:
                            f.write("integer height = 84\n")
                        widthProp = False
                        heightProp = False
                        endType = False
                    f.write(line.rstrip())
                    f.write("\n")
