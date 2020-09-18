import os

dirs = os.listdir(".")
removedItemCount = 0

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
       if name.endswith(".srd") or name.endswith(".srf") or name.endswith(".sru") or name.endswith(".srw") or name.endswith(".srs") or name.endswith(".srm") or name.endswith(".srq"):
        fileName = os.path.join(root, name)
        print(fileName)
        os.remove(fileName)
        removedItemCount = removedItemCount + 1

print("Removed: " + str(removedItemCount))
