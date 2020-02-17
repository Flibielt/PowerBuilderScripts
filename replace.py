import codecs
import os
import enum

class SetterInsertion(enum.Enum):
    wait = 1
    done = 2
    insert = 3
    witchConstructor = 4

setterInsertion = SetterInsertion.done
uGomb = False
skipLine = False
uGombEvents = False
setterFuncs = {""}

for root, dirs, files in os.walk("..\\mc2svn17UD", topdown=False):
   for name in files:
      if name.startswith("w_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_gomb within" in line:
                    line = line.replace("u_gomb", "u_dynamic_button")
                    uGomb = True
                    uGombEvents = False
                    if setterInsertion == SetterInsertion.wait:
                        setterInsertion = SetterInsertion.witchConstructor
                elif "end type" in line:
                    uGomb = False
                    uGombEvents = True
                    setterInsertion = SetterInsertion.wait
                #Convert some properties to setters
                if uGomb:
                    if "int textsize" in line.lower() or "integer textsize" in line.lower():
                        setterFuncs.add("this.set_textsize(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "string text" in line.lower() or "string Text" in line:
                        setterFuncs.add("this.set_text(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "fontcharset fontcharset" in line.lower():
                        setterFuncs.add("this.set_fontcharset(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "fontfamily fontfamily" in line.lower():
                        setterFuncs.add("this.set_fontfamily(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "fontpitch fontpitch" in line.lower():
                        setterFuncs.add("this.set_fontpitch(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "string facename" in line.lower():
                        setterFuncs.add("this.set_facename(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "integer weight" in line.lower() or "int weight" in line.lower():
                        setterFuncs.add("this.set_weight(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "string powertiptext" in line.lower():
                        setterFuncs.add("this.add_powertip(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "string tag" in line.lower():
                        setterFuncs.add("this.set_tag(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                    elif "boolean default" in line.lower():
                        setterFuncs.add("this.set_default(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                        #Add functionality
                    elif "boolean cancel" in line.lower():
                        setterFuncs.add("this.set_cancel(" + line[line.find("="):].strip() + ")")
                        skipLine = True
                        #Add functionality
                    elif "boolean ib_ugomb2" in line.lower():
                        skipLine = True
                        #More functionality?
                
                if uGombEvents:
                    if "event clicked;call super::clicked;" in line.lower():
                        line = line.replace("event clicked;call super::clicked;", "event u_click;call super::u_click;")
                    elif "event constructor;call super::constructor;" in line.lower():
                        setterInsertion = SetterInsertion.insert
                    elif line.strip().startswith("type") and setterInsertion == SetterInsertion.wait:
                        setterInsertion = SetterInsertion.witchConstructor
                    elif line.strip().startswith("type"):
                        uGombEvents = False

                if not skipLine:
                    with open(outFile, "a") as f:
                        if setterInsertion == SetterInsertion.insert:
                            f.write(line.rstrip())
                            f.write("\n")
                            for setter in setterFuncs:
                                f.write(setter)
                                f.write("\r")
                            setterFuncs.clear()
                            setterInsertion = SetterInsertion.done
                        elif setterInsertion == SetterInsertion.witchConstructor:
                            f.write("event constructor;call super::constructor;")
                            f.write("\r")
                            for setter in setterFuncs:
                                f.write(setter)
                                f.write("\r")
                            f.write("end event")
                            f.write("\r")
                            f.write("\r")
                            f.write(line.rstrip())
                            f.write("\r")
                            setterFuncs.clear()
                            setterInsertion = SetterInsertion.done
                        else:
                            f.write(line.rstrip())
                            f.write("\n")
                skipLine = False
