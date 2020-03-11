import codecs
import os

for root, dirs, files in os.walk("folderName", topdown=False):
   for name in files:
      if name.startswith("w_") or name.startswith("u"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        button = False
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if " type cb_" in line or " type pb_" in line:
                    button = True
                elif " type " in line:
                    button = False
                
                if button:
                    if " clicked " in line.lower() or "::clicked" in line.lower() or " clicked;" in line.lower():
                        line.replace("clicked", "u_click")
                
                with open(outFile, "a") as f:
                    f.write(line.rstrip())
                    f.write("\n")