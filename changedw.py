import codecs
import os

for root, dirs, files in os.walk("..\\medikai", topdown=False):
   for name in files:
      if name.startswith("d_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out_d" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "font.face" in line.lower():
                    print(line.split("font.face=\"")[1])
