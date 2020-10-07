import os

def clearProject(projectFolder):
    removedItemCount = 0

    for root, dirs, files in os.walk(projectFolder, topdown=False):
        for name in files:
            if name.endswith(".srd") or name.endswith(".srf") or name.endswith(".sru") or name.endswith(".srw") or name.endswith(".srs") or name.endswith(".srm") or name.endswith(".srq"):
                fileName = os.path.join(root, name)
                print(fileName)
                os.remove(fileName)
                removedItemCount = removedItemCount + 1

    print("Removed: " + str(removedItemCount))

def deleteEmptyFolders(projectFolder):
    for root, dirs, files in os.walk(projectFolder, topdown=False):
        for name in files:
            try:
                if len(os.listdir( os.path.join(root, name) )) == 0:
                    try:
                        os.rmdir(os.path.join(root, name))
                    except:
                        print( "Failed to delete:", os.path.join(root, name) )
            except:
                pass
