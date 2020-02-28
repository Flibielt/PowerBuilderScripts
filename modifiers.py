import codecs
import os

modifiedTypes = {""}
filesAffected = {""}
prop = False

for root, dirs, files in os.walk("..\\medikai", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        #print(fileName)
        modifiedTypes.clear()
        if "d_" not in fileName:
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    if ".width" in line.lower() or ".height" in line.lower() or ".x" in line.lower() or ".y" in line.lower() or ".textsize" in line.lower():
                        filesAffected.add(fileName)
                        #print(line.strip())
                
for f in filesAffected:
    print(f)
print("Files affected: " + str(len(filesAffected)))