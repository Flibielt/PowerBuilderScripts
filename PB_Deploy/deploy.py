import codecs
import os
import stat
import sys, getopt
import distutils
from shutil import copyfile

from getPBDfiles import getPBDFiles
from clear import clearProject, deleteEmptyFolders
from copySvn import copySvn

project = ""
projectFolder = ""
svnFolder = ""
libraryCount = 0
command = ""

"""
if len(sys.argv) == 0:
    print("Project name is needed")
    sys.exit(0)
else:
    project = sys.argv[1]
"""
project = "medboss"

with codecs.open("properties.txt", encoding='utf8') as f:
    for line in f:
        if project in line:
            projectFolder = line.replace(project + ":", "")
        elif "svn" in line:
            svnFolder = line.replace("svn:", "")

if len(projectFolder) == 0:
    print("Wrong project name")
    sys.exit(0)
else:
    project = project.strip().replace("\\", "/")
    projectFolder = projectFolder.strip().replace("\\", "/")
    svnFolder = svnFolder.strip().replace("\\", "/")
    print("Project: " + project)
    print("Project folder: " + projectFolder)
    print("SVN folder: " + svnFolder)

libraryCount = copySvn(project, projectFolder, svnFolder)
COM, DES, CPY, PVS, PVN, PRD, PBT, EXE = "", "", "", "", "", "", "", ""
srjFile = ""
lineCount = 1

for root, dirs, files in os.walk(projectFolder):
    for file in files:
        if file.endswith(".srj") and project in file:
            print("SRJ file:")
            print(os.path.join(root, file))
            srjFile = os.path.join(root, file)
            srjFile = srjFile.replace("\\", "/")
        elif file.endswith(".pbt"):
            print("PBT file:")
            print(os.path.join(root, file))
            PBT = os.path.join(root, file)
            PBT = PBT.replace("\\", "/")
            os.chmod(PBT, stat.S_IWRITE)
            PBT = PBT.replace("/", "\\")

EXE = projectFolder + "/EXE/" + project + ".exe"
EXE = EXE.replace("/", "\\")

with codecs.open(srjFile, encoding='utf8') as f:
    for line in f:
        print(line.rstrip())
        if lineCount == 5:
            COM = line[4:].lstrip()
            COM = COM.replace("\r\n", "")
            COM = COM.strip()
        elif lineCount == 6:
            DES = line[4:].lstrip()
            DES = DES.replace("\r\n", "")
            DES = DES.strip()
        elif lineCount == 7:
            CPY = line[4:].lstrip()
            CPY = CPY.replace("\r\n", "")
            CPY = CPY.strip()
        elif lineCount == 8:
            PRD = line[4:].lstrip()
            PRD = PRD.replace("\r\n", "")
            PRD = PRD.strip()
        elif lineCount == 9:
            PVS = line[4:].lstrip()
            PRD = PRD.replace("\r\n", "")
            PRD = PRD.strip()
        elif lineCount == 10:
            PVN = line[4:].lstrip()
            PRD = PRD.replace("\r\n", "")
            PRD = PRD.strip()
        elif "OBJ:" in line:
            break
        lineCount = lineCount + 1

with codecs.open("deploy.txt", encoding='utf8') as f:
    for line in f:
        line = line.replace("@COM", COM)
        line = line.replace("@DES", DES)
        line = line.replace("@CPY", CPY)
        line = line.replace("@PRD", PRD)
        line = line.replace("@PVS", PVS)
        line = line.replace("@PVN", PVN)
        line = line.replace("@SRJ", PBT)
        line = line.replace("@EXE", EXE)
        line = line.replace("@PBT", PBT)
        command = line

command = command + " " + 'y' * libraryCount
#command = command + " " + 'y' * 179

print(command)

os.system('cmd /c ' + command)

getPBDFiles(projectFolder)
clearProject(projectFolder)
