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
uGombDeclaration = False
skipLine = False
decleration = False
uGombEvents = False
setterFuncs = {""}

#todo: window szinten esc/enter esetén default/cacnel trigger
#todo: property változás helyett setterek a deklarációkon kívül is
#todo: cb_ok.Event Post Clicked() helyett cb_ok.Event Post u_click(1, 1, 1)
#todo: width és height property legyen mindenhol

for root, dirs, files in os.walk("..\\medikai", topdown=False):
   for name in files:
      if name.startswith("w_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_gomb within" in line or "from commandbutton within" in line or "from u_ok_gomb within" in line or "from u_megsem_gomb within" in line or "from w_adatbevalap`cb_" in line:
                    line = line.replace("u_gomb", "u_dynamic_button")
                    line = line.replace("commandbutton", "u_dynamic_button")
                    line = line.replace("u_ok_gomb", "u_dynamic_button")
                    line = line.replace("u_megsem_gomb", "u_dynamic_button")
                    uGomb = True
                    uGombEvents = False
                    if setterInsertion == SetterInsertion.wait:
                        setterInsertion = SetterInsertion.witchConstructor
                elif "end type" in line and uGomb == True:
                    uGomb = False
                    uGombEvents = True
                    setterInsertion = SetterInsertion.wait
                #Convert some properties to setters
                elif uGomb:
                    if "int textsize" in line.lower() or "integer textsize" in line.lower():
                        setterFuncs.add("this.set_textsize(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "string text" in line.lower() or "string Text" in line:
                        setterFuncs.add("this.set_text(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "fontcharset fontcharset" in line.lower():
                        setterFuncs.add("this.set_fontcharset(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "fontfamily fontfamily" in line.lower():
                        setterFuncs.add("this.set_fontfamily(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "fontpitch fontpitch" in line.lower():
                        setterFuncs.add("this.set_fontpitch(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "string facename" in line.lower():
                        setterFuncs.add("this.set_facename(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "integer weight" in line.lower() or "int weight" in line.lower():
                        setterFuncs.add("this.set_weight(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "string powertiptext" in line.lower():
                        setterFuncs.add("this.add_powertip(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "string tag" in line.lower():
                        setterFuncs.add("this.set_tag(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "boolean default" in line.lower():
                        setterFuncs.add("this.set_default(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "boolean cancel" in line.lower():
                        setterFuncs.add("this.set_cancel(" + line[line.find("=") + 1:].strip() + ")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "boolean ib_ugomb2" in line.lower():
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "integer x" in line.lower() or "int x" in line.lower() or "integer y" in line.lower() or "int y" in line.lower():
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                    
                if uGombEvents:
                    if "event clicked;call super::clicked;" in line.lower():
                        line = line.replace("event clicked;call super::clicked;", "event u_click;call super::u_click;")
                    elif "event clicked;" in line.lower():
                        line = line.replace("event clicked;", "event u_click;call super::u_click;")
                    elif "event constructor;call super::constructor;" in line.lower():
                        setterInsertion = SetterInsertion.insert
                    elif line.strip().startswith("type") and setterInsertion == SetterInsertion.wait:
                        setterInsertion = SetterInsertion.witchConstructor
                        uGombEvents = False
                    elif line.strip().startswith("type"):
                        uGombEvents = False

                if (";cb_" in repr(line) and "." in repr(line) and "=" in repr(line)):
                    if not "enabled" in line.lower() and not ".x" in line.lower() and not ".y" in line.lower() and not ".visible" in line.lower() and not ".taborder" in line.lower() and not ".bringtotop" in line.lower():
                        line = line[:line.find("=") - 1].rstrip() + ".(" + line[line.find("=") + 1:].strip() + ")"
                
                if (line.strip().startswith("cb_") and "." in repr(line) and "=" in repr(line)):
                    if not "enabled" in line.lower() and not ".x" in line.lower() and not ".y" in line.lower() and not ".visible" in line.lower() and not ".taborder" in line.lower() and not ".bringtotop" in line.lower():
                        line = line[:line.find("=") - 1].strip() + ".(" + line[line.find("=") + 1:].strip() + ")"

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
                        elif setterInsertion == SetterInsertion.witchConstructor and line.lower().startswith("type"):
                            validSetter = False
                            for setter in setterFuncs:
                                if "this." in setter:
                                    validSetter = True
                            
                            if validSetter:
                                f.write("event constructor;call super::constructor;")
                                f.write("\r")
                                for setter in setterFuncs:
                                    f.write(setter)
                                    f.write("\r")
                                f.write("end event")
                                f.write("\r")
                                f.write("\n")
                                setterFuncs.clear()
                            setterInsertion = SetterInsertion.done
                            f.write(line.rstrip())
                            f.write("\r")
                        else:
                            f.write(line.rstrip())
                            f.write("\n")
                skipLine = False
            
            #If the button is the last element
            validSetter = False
            for setter in setterFuncs:
                if "this." in setter:
                    validSetter = True
            if validSetter:
                with open(outFile, "a") as f:
                    f.write("event constructor;call super::constructor;")
                    f.write("\r")
                    for setter in setterFuncs:
                        f.write(setter)
                        f.write("\r")
                    f.write("end event")
                    f.write("\r")
                    f.write("\n")
                    setterFuncs.clear()
                    setterInsertion = SetterInsertion.done
