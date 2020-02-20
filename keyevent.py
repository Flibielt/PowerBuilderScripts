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
                if "from u_dynamic_button within" in line:
                    buttons.add(line[line.find("type ") + 4:line.find(" from")].strip())
        
        with codecs.open(fileName, encoding='utf8') as f:
            endCount = 0
            for line in f:
                with open(outFile, "a") as f:
                    if "end on" in line:
                        endCount = endCount + 1
                    
                    if endCount == 2:
                        print("Insert key event")



for button in buttons:
    print(button)