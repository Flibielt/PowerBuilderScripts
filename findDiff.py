import codecs
import os
from shutil import copyfile

diffFiles = {""}
is4DiffFiles = {""}

with codecs.open("diff.txt", encoding='utf8') as f:
    for line in f:
        line = line[1:]
        line = line.strip()
        diffFiles.add(line)

with codecs.open("is4Mod.txt", encoding='utf8') as f:
    for line in f:
        is4DiffFiles.add(line)

for modified in is4DiffFiles.difference(diffFiles):
    print (modified)
