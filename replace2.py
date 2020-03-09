import codecs
import os

for root, dirs, files in os.walk(".\\", topdown=False):
   for name in files:
      if name.startswith("w_") or name.startswith("u"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        dynamicButton = False
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_dynamic_button" in line:
                    dynamicButton = True
                if "`" in line:
                    # cb: CommandButton
                    # pb: PictureButton
                    if "type cb_" in line or "type pb_" in line:
                        dynamicButton = True
                if dynamicButton == True:
                    if line.strip().startswith("event") and "clicked" in line and "doubleclicked" not in line and "rightclicked" not in line:
                       line = line.replace("clicked", "u_click")
                       dynamicButton = False
                if "u_dynamic_button2" in line:
                    line = line.replace("u_dynamic_button2", "u_dynamic_button")
                
                with open(outFile, "a") as f:
                    f.write(line.rstrip())
                    f.write("\n")