import codecs
import os
import distutils
import sys
import stat
from shutil import copyfile
from distutils import dir_util

def copySvn(projectName, projectFolder, svnFolder):
    pbtFile = svnFolder + "/" + projectName + ".pbt"
    libraryList = ""

    os.chmod(pbtFile, stat.S_IWRITE)
    copyfile(pbtFile, projectFolder + "/" + projectName + ".pbt")

    with codecs.open(pbtFile, encoding='utf8') as f:
        for line in f:
            if "LibList" in line:
                libraryList = line
                libraryList = libraryList.replace("LibList \"", "")
                libraryList = libraryList.replace("\";", "")
                libraries = libraryList.split(";")
    
    for library in libraries:
        library = library.replace("\\\\", "/")
        folder = svnFolder + "/" + library
        folder = folder[:folder.rfind("/")]
        dest = projectFolder + "/" + library
        dest = dest[:dest.rfind("/")]
        dir_util.copy_tree(folder, dest)
    
    return len(libraries) + 1