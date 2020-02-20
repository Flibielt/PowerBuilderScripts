import codecs
import os

buttons = {""}
buttonProp = False

for root, dirs, files in os.walk("..\\medikai", topdown=False):
   for name in files:
      if name.startswith("w_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_gomb within" in line or "from commandbutton within" in line or "from u_ok_gomb within" in line or "from u_megsem_gomb within" in line or "from w_adatbevalap`cb_" in line:
                    buttons.add(line[line.find("type ") + 4:line.find(" from")].strip())
                    buttonProp = True
                elif buttonProp:
                    if "end type" in line:
                        buttonProp = False
                    else:
                        
                

for button in buttons:
    print(button)