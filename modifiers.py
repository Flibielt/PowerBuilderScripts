import codecs
import os

for root, dirs, files in os.walk("..\\medikai", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                print(repr(line))