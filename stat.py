import codecs
import os

singleEdit = 0
multiEdit = 0
lineCount = 0
fileCount = 0

for root, dirs, files in os.walk("..\\mc2svn17UD", topdown=False):
   for name in files:
      if not ".svn" in root:
         fileCount = fileCount + 1
         fileName = os.path.join(root, name)
         print(fileName)
         with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                lineCount = lineCount + 1
                if "from u_multilinedit" in line:
                    multiEdit = multiEdit + 1
                elif "from u_sledit" in line or "from u_sledit_bekuldokod" in line or "from u_sledit_dwfind" in line:
                    singleEdit = singleEdit + 1

print("File count: " + str(fileCount))
print("Line count: " + str(lineCount))
print("SingleLineEdit count: " + str(singleEdit))
print("MultilineEdit count: " + str(multiEdit))

