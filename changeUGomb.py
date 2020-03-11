import codecs
import os

for root, dirs, files in os.walk("folderName", topdown=False):
   for name in files:
      if name.startswith("w_") or name.startswith("u"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        uGomb = False
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if " from u_gomb " in line or " from commandbutton " in line or " from picturebutton " in line:
                    line = line.replace("u_gomb", "u_dynamic_button")
                    uGomb = True
                elif " from " in line and " u_gomb " not in line:
                    uGomb = False
                
                if uGomb:
                    if " clicked " in line.lower() and "::clicked" in line.lower():
                        line.replace("clicked", "u_click")
                
                with open(outFile, "a") as f:
                    f.write(line.rstrip())

