import codecs
import os

for root, dirs, files in os.walk("folderName", topdown=False):
   for name in files:
      if name.startswith("w_") or name.startswith("u"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out2" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        dynamicButton = False
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_dynamic_button" in line:
                    dynamicButton = True
                elif " from " in line and "dynamic_button" not in line:
                    dynamicButton = False
                elif dynamicButton:
                    if line.strip().startswith("event") and "clicked" in line:
                        line.replace("clicked", "u_click")
                
                if "u_dynamic_button2" in line:
                    line.replace("u_dynamic_button2", "u_dynamic_button")