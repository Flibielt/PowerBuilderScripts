import codecs
import os

constProp = {""}
dynamicButton = False
dynamicButtonProp = False
skipLine = False
constructorExist = False

for root, dirs, files in os.walk("proba", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        dynamicButton = False
        skipLine = False
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if " from u_dynamic_button within ":
                    dynamicButton = True
                    dynamicButtonProp = True
                    constProp.add("this.resize_inner_objects(this.width, this.height)")
                elif " cb_" in line.lower() or " pb_" in line.lower():
                    if "`" in line.lower():
                        dynamicButton = True
                        dynamicButtonProp = True
                        constProp.add("this.resize_inner_objects(this.width, this.height)")
                
                if dynamicButtonProp == True:
                    if "textsize" in line.lower() and "=" in line:
                        constProp.add("this.set_textsize(" + line[line.find("=") + 1:].strip() + ")")
                        constProp.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "string powertiptext" in line.lower() and "=" in line:
                        constProp.add("this.add_powertip(" + line[line.find("=") + 1:].strip() + ")")
                        constProp.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "string text" in line.lower() and "=" in line:
                        constProp.add("this.set_text(" + line[line.find("=") + 1:].strip() + ")")
                        constProp.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "string tag" in line.lower():
                        constProp.add("this.set_tag(" + line[line.find("=") + 1:].strip() + ")")
                        constProp.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "boolean default" in line.lower():
                        constProp.add("this.set_default(" + line[line.find("=") + 1:].strip() + ")")
                        constProp.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "boolean cancel" in line.lower():
                        constProp.add("this.set_cancel(" + line[line.find("=") + 1:].strip() + ")")
                        constProp.add("this.resize_inner_objects(this.width, this.height)")
                        skipLine = True
                    elif "end type" in line.lower():
                        dynamicButtonProp = False
                
                if dynamicButton and line.strip().startswith("type") and "u_dynamic_button" not in line:
                    dynamicButton = False
            
                if not skipLine:
                    with open(outFile, "a") as f:
                        insertSetter = False
                        insertConst = False
                        if dynamicButton == True:
                            if " event " in line.lower() and "constructor" in line.lower():
                                insertSetter = True
                        elif dynamicButton == False and len(constProp) > 1:
                            insertConst = True
                        elif insertSetter == True:
                            f.write(line.rstrip())
                            f.write("\n")
                            for settter in constProp:
                                f.write(settter)
                                f.write("\n")
                            constProp.clear()
                        elif insertConst == True:
                            f.write("event constructor;call super::constructor;")
                            f.write("\n")
                            for setter in constProp:
                                f.write(setter)
                                f.write("\n")
                            constProp.clear()

                            f.write("end event")
                            f.write("\n")
                            f.write("\n")
                        else:
                            f.write(line.rstrip())
                            f.write("\n")
                skipLine = False

