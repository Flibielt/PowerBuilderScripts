import codecs
import os

for root, dirs, files in os.walk("folder", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "proba_out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        lastLine = ""
        setters = {""}
        if name.startswith("w_") or name.startswith("uov_"):
            button = False
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    if button and " from " in line:
                        validConst = False
                        for setter in setters:
                            if "this." in setter:
                                validConst = True
                        if validConst:
                            with open(outFile, "a") as fOut:
                                fOut.write("event constructor;call super::constructor;")
                                fOut.write("\n")
                                for setter in setters:
                                    fOut.write(setter)
                                    fOut.write("\n")
                                fOut.write("end event")
                                fOut.write("\n")
                                fOut.write("\n")
                        button = False
                        setters.clear()

                    if "from u_kk_commandbutton" in line:
                        button = True
                        line = line.replace("u_kk_commandbutton_bezar", "u_dynamic_button")
                        line = line.replace("u_kk_commandbutton", "u_dynamic_button")
                        setters.add("this.resize_inner_objects(this.width, this.height)")
                    elif "end type" in line and " within " in line:
                        setters.clear()
                        button = False
                    elif button:
                        if "int textsize" in line.lower() or "integer textsize" in line.lower():
                            setters.add("this.set_textsize(" + line[line.find("=") + 1:].strip() + ")")
                            skipLine = True
                        elif "string text" in line.lower() or "string Text" in line:
                            setters.add("this.set_text(" + line[line.find("=") + 1:].strip() + ")")
                            setters.add("this.resize_inner_objects(this.width, this.height)")
                            skipLine = True
                        elif "integer weight" in line.lower() or "int weight" in line.lower():
                            setters.add("this.set_weight(" + line[line.find("=") + 1:].strip() + ")")
                            setters.add("this.resize_inner_objects(this.width, this.height)")
                            skipLine = True
                        elif "string powertiptext" in line.lower():
                            setters.add("this.add_powertip(" + line[line.find("=") + 1:].strip() + ")")
                            setters.add("this.resize_inner_objects(this.width, this.height)")
                            skipLine = True
                        elif "string tag" in line.lower():
                            setters.add("this.set_tag(" + line[line.find("=") + 1:].strip() + ")")
                            setters.add("this.resize_inner_objects(this.width, this.height)")
                            skipLine = True
                        elif "boolean default" in line.lower():
                            setters.add("this.set_default(" + line[line.find("=") + 1:].strip() + ")")
                            setters.add("this.resize_inner_objects(this.width, this.height)")
                            skipLine = True
                        elif "boolean cancel" in line.lower():
                            setters.add("this.set_cancel(" + line[line.find("=") + 1:].strip() + ")")
                            setters.add("this.resize_inner_objects(this.width, this.height)")
                            skipLine = True
                        elif "constructor" in lastLine:
                            with open(outFile, "a") as fOut:
                                for setter in setters:
                                    fOut.write(setter)
                                    fOut.write("\n")
                            setters.clear()
                            button = False
                
                if button:
                    validConst = False
                    for setter in setters:
                        if "this." in setter:
                            validConst = True
                        
                        if validConst:
                            with open(outFile, "a") as fOut:
                                fOut.write("event constructor;call super::constructor;")
                                fOut.write("\n")
                                for setter in setters:
                                    fOut.write(setter)
                                    fOut.write("\n")
                                fOut.write("end event")
                                fOut.write("\n")
                                fOut.write("\n")
                        button = False
                        setters.clear()
