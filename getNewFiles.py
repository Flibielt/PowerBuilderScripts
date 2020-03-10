import codecs
import os
from shutil import copyfile

diffFiles = []

with codecs.open("diff.txt", encoding='utf8') as f:
   for line in f:
      diffFiles.append(line.strip())
      #print(line.rstrip())

count = 0
for root, dirs, files in os.walk("currentLatest", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        #print(fileName)
        outFile = "diff" + fileName[fileName.find("\\"):]
        if fileName in diffFiles:
            os.makedirs(os.path.dirname(outFile), exist_ok=True)
            print(os.path.dirname(outFile))
            count = count + 1
            diffFiles.pop(diffFiles.index(fileName))
            copyfile(fileName.replace("\\", "/"), outFile)

print(count)

for diff in diffFiles:
   print(diff)
