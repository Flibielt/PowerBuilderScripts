# !/usr/bin/python
import codecs
import os

buttonSet = {"gomb1"}
buttonRepeat = 0
uGombSet = {"gomb1"}
uGombRepeat = 0
uGomb2Set = {"gomb1"}
uGomb2Repeat = 0
uGomb = False
uGombDeclaration = False
uGombEvenetDeclaration = False
uGombProperties = {"prop"}
uGombEvents = {"event"}

for root, dirs, files in os.walk("..\\mc2svn17UD", topdown=False):
   for name in files:
      if name.startswith("w_"):
         fileName = os.path.join(root, name)
         print(fileName)
         with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
               if uGomb:
                  if "end type" in repr(line):
                     uGombDeclaration = False
                     uGomb = False
                     uGombEvenetDeclaration = True
                  else:
                     uGombDeclaration = True
                  if uGombDeclaration:
                     if not repr(line).startswith("'event"):
                        uGombProperties.add(repr(line)[1:repr(line).find("=")])

               if uGombEvenetDeclaration:
                  if "end type" in repr(line):
                     uGombEvenetDeclaration = True
                  elif "type" in repr(line):
                     uGombEvenetDeclaration = False

               if uGombEvenetDeclaration:
                  if "'event" in repr(line):
                     #print(repr(line))
                     uGombEvents.add(repr(line)[1:repr(line).find(";")])
               
               if "type cb_" in repr(line):
                  if "from commandbutton" in repr(line) or "from picturebutton" in repr(line):
                     #print(repr(line))
                     buttonSet.add(repr(line))
                     buttonRepeat = buttonRepeat + 1
                     u_gomb = True
                  elif "from u_gomb " in repr(line):
                     #print(repr(line))
                     uGombSet.add(repr(line))
                     uGombRepeat = uGombRepeat + 1
                     uGomb = True
                  elif "from u_gomb2" in repr(line):
                     #print(repr(line))
                     uGomb2Set.add(repr(line))
                     uGomb2Repeat = uGomb2Repeat + 1
                  
buttonSet.remove("gomb1")
uGombSet.remove("gomb1")
uGomb2Set.remove("gomb1")
uGombProperties.remove("prop")
uGombEvents.remove("event")
buttonRepeat = buttonRepeat - len(buttonSet)
uGombRepeat = uGombRepeat - len(uGombSet)
uGomb2Repeat = uGomb2Repeat - len(uGomb2Set)
print("Number of buttons: " + str(len(buttonSet)))
#print("Repeat: " + str(buttonRepeat))
print("Number of u_gomb: " + str(len(uGombSet)))
#print("Repeat: " + str(uGombRepeat))
print("Number of u_gomb2: " + str(len(uGomb2Set)))
#print("Repeat: " + str(uGomb2Repeat))

print("\nu_gomb properties:")
print("Count: " + str(len(uGombProperties)))
for prop in uGombProperties:
   print(prop)

print("\nu_gomb events:")
print("Count: " + str(len(uGombEvents)))
for event in uGombEvents:
   print(event)

