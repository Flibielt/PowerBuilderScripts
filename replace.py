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
okGomb = False
megsemGomb = False
skipLine = False
decleration = False
uGombEvents = False
clickEvent = False
clickEventIfInserted = False
setterFuncs = {""}

#todo: window szinten esc/enter esetén default/cacnel trigger
#todo: property változás helyett setterek a deklarációkon kívül is

for root, dirs, files in os.walk("..\\mc2svn17UD", topdown=False):
   for name in files:
      if name.startswith("w_") or name.startswith("u"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out2" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_gomb within" in line or "from commandbutton within" in line or "from u_ok_gomb within" in line or "from u_megsem_gomb within" in line or "from w_adatbevalap`cb_" in line or "from picturebutton" or "uov_gomb" in line or "uov_ok_gomb" in line:
                    if "ok_gomb" in line or "_ok" in line:
                        okGomb = True
                    elif "megsem" in line:
                        megsemGomb = True
                    line = line.replace("u_gomb", "u_dynamic_button")
                    line = line.replace("commandbutton", "u_dynamic_button")
                    line = line.replace("picturebutton", "u_dynamic_button")
                    line = line.replace("u_ok_gomb", "u_dynamic_button")
                    line = line.replace("u_megsem_gomb", "u_dynamic_button")
                    line = line.replace("uov_gomb", "u_dynamic_button")
                    line = line.replace("uov_ok_gomb", "u_dynamic_button")
                    uGomb = True
                    uGombEvents = False
                    if setterInsertion == SetterInsertion.wait:
                        setterInsertion = SetterInsertion.witchConstructor
                elif "end type" in line and uGomb == True:
                    okGomb = False
                    megsemGomb = False
                    uGomb = False
                    uGombEvents = True
                    setterInsertion = SetterInsertion.wait
                elif "string facename" in line.lower():
                    line = line[:line.find("\"")] +  "\"DINPro-Medium\""
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
                        setterFuncs.add("this.set_fontcharset(\"" + line[line.find("=") + 1:].strip() + "\")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "fontfamily fontfamily" in line.lower():
                        setterFuncs.add("this.set_fontfamily(\"" + line[line.find("=") + 1:].strip() + "\")")
                        setterFuncs.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "fontpitch fontpitch" in line.lower():
                        setterFuncs.add("this.set_fontpitch(\"" + line[line.find("=") + 1:].strip() + "\")")
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
                        if okGomb:
                            setterFuncs.add("this.set_text(\"OK\")")
                        elif megsemGomb:
                            setterFuncs.add("this.set_text(\"&M$$HEX1$$e900$$ENDHEX$$gsem\")")
                    
                if uGombEvents:
                    if "clicked;call super::clicked;" in line.lower():
                        line = line.replace("clicked;call super::clicked;", "u_click;call super::u_click;")
                        clickEvent = True
                        clickEventIfInserted = False
                    elif "clicked;" in line.lower():
                        line = line.replace("clicked;", "u_click;call super::u_click;")
                        clickEvent = True
                        clickEventIfInserted = False
                    elif "event cb_ok::clicked" in line.lower():
                        line = line.replace("event cb_ok::clicked;", "event cb_ok::u_click;")
                        clickEvent = True
                        clickEventIfInserted = False
                    elif "event cb_ok::clicked;call super::clicked;" in line.lower():
                        line = line.replace("event cb_ok::clicked;call super::clicked;", "event cb_ok::u_click;")
                        clickEvent = True
                        clickEventIfInserted = False
                    elif "event ue_postclicked;" in line.lower():
                        line = line.replace("ue_postclicked", "u_click")
                        clickEvent = True
                        clickEventIfInserted = False
                    elif "event constructor;call super::constructor;" in line.lower():
                        setterInsertion = SetterInsertion.insert
                    elif line.strip().startswith("type") and setterInsertion == SetterInsertion.wait:
                        setterInsertion = SetterInsertion.witchConstructor
                        uGombEvents = False
                    elif line.strip().startswith("type"):
                        uGombEvents = False

                if (";cb_" in repr(line) and "." in repr(line) and "=" in repr(line)):
                    if ".default" in line.lower():
                        line = line.lower().replace(".default", ".set_default(")
                        line = line[:line.find("=") - 1].rstrip() + line[line.find("=") + 1:].strip() + ")\n"
                    elif ".cancel" in line.lower():
                        line = line.lower().replace(".cancel", ".set_cancel(")
                        line = line[:line.find("=") - 1].rstrip() + line[line.find("=") + 1:].strip() + ")\n"
                
                if (line.strip().startswith("cb_") and "." in repr(line) and "=" in repr(line)):
                    if ".default" in line.lower():
                        line = line.lower().replace(".default", ".set_default(")
                        line = line[:line.find("=") - 1].rstrip() + line[line.find("=") + 1:].strip() + ")\n"
                    elif ".cancel" in line.lower():
                        line = line.lower().replace(".cancel", ".set_cancel(")
                        line = line[:line.find("=") - 1].rstrip() + line[line.find("=") + 1:].strip() + ")\n"

                if "cb_" in line and ".event post clicked()" in line.lower():
                    line = line.lower().replace("clicked()", "u_click(1, 1, 1)")
                elif "cb_" in line and ".event clicked()" in line.lower():
                    line = line.lower().replace("clicked()", "u_click(1, 1, 1)")
                elif "cb_" in line and ".event ue_postclicked()" in line.lower():
                    line = line.lower().replace("ue_postclicked", "u_click(1, 1, 1)")

                if "pb_" in line and ".event post clicked()" in line.lower():
                    line = line.lower().replace("clicked()", "u_click(1, 1, 1)")
                elif "pb_" in line and ".event clicked()" in line.lower():
                    line = line.lower().replace("clicked()", "u_click(1, 1, 1)")
                elif "pb_" in line and ".event ue_postclicked()" in line.lower():
                    line = line.lower().replace("ue_postclicked", "u_click(1, 1, 1)")

                if not skipLine:
                    with open(outFile, "a") as f:
                        if setterInsertion == SetterInsertion.insert:
                            f.write(line.rstrip())
                            f.write("\n")
                            for setter in setterFuncs:
                                f.write(setter)
                                f.write("\n")
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
                                    f.write("\n")
                                f.write("end event")
                                f.write("\n")
                                setterFuncs.clear()
                            setterInsertion = SetterInsertion.done
                            f.write(line.rstrip())
                            f.write("\n")
                        else:
                            if clickEvent:
                                if not clickEventIfInserted and "super::u_click;":
                                    line = line.replace("super::u_click;", "super::u_click; if this.enabled = true and (isNull(flags) or (flags = 5 and this.is_cancel()) or (flags = 6 and this.is_default())) then\n")
                                    f.write(line.rstrip())
                                    f.write("\n")
                                    clickEventIfInserted = True
                                elif "end event" in line:
                                    f.write("end if\n")
                                    f.write(line.rstrip())
                                    f.write("\n")
                                    clickEvent = False
                                else:
                                    f.write(line.rstrip())
                                    f.write("\n")
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
                    f.write("\n")
                    for setter in setterFuncs:
                        f.write(setter)
                        f.write("\n")
                    f.write("end event")
                    f.write("\r")
                    f.write("\n")
                    setterFuncs.clear()
                    setterInsertion = SetterInsertion.done
