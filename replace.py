import codecs
import os

uGomb = False
skipLine = False
setterFuncs = {""}
defaultButtons = {""}
cancelButtons = {""}

for root, dirs, files in os.walk("mc2svn17UD", topdown=False):
   for name in files:
      if name.startswith("w_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_gomb within" in line:
                    line = line.replace("u_gomb", "u_dynamic_button")
                    uGomb = True
                elif uGomb and "end type" in line:
                    uGomb = False
                #Convert some properties to setters
                if uGomb:
                    if "int textsize" in line.lower() or "integer textsize" in line.lower():
                        setterFuncs.add("this.set_textsize(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "string Text " in line.lower():
                        setterFuncs.add("this.set_text(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "fontcharset fontcharset" in line.lower():
                        setterFuncs.add("this.set_fontcharset(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "fontfamily fontfamily" in line.lower():
                        setterFuncs.add("this.set_fontfamily(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "fontpitch fontpitch" in line.lower():
                        setterFuncs.add("this.set_fontpitch(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "string facename" in line.lower():
                        setterFuncs.add("this.set_facename(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "integer weight" in line.lower() or "int weight" in line.lower():
                        setterFuncs.add("this.set_weight(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "string powertiptext" in line.lower():
                        setterFuncs.add("this.add_powertip(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "string tag" in line.lower():
                        setterFuncs.add("this.set_tag(" + line[line.find["= ":]].strip() + ")")
                        skipLine = True
                    elif "boolean default" in line.lower():
                        defaultButtons.add("button name")
                        skipLine = True
                        #Add functionality
                    elif "boolean cancel" in line.lower():
                        cancelButtons.add("button name")
                        skipLine = True
                        #Add functionality
                    elif "boolean ib_ugomb2" in line.lower():
                        skipLine = True
                        #More functionality?
                

                if not skipLine:
                    with open(outFile, "a") as f:
                        f.write(line.rstrip())
                        f.write("\n")