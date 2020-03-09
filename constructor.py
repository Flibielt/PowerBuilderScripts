import codecs
import os

constProp = {""}
dynamicButton = False
dynamicButtonProp = False
skipLine = False
newButton = False
isDef = False

for root, dirs, files in os.walk("folderName", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "folderName_out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        dynamicButton = False
        skipLine = False
        constProp.clear()
        endSetters = False
        if name.startswith("w_") or name.startswith("uov_") or name.startswith("u_"):
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    if "end forward" in line.lower():
                        dynamicButton = False
                        dynamicButtonProp = False
                        constProp.clear()
                    
                    if "end type" in line.lower():
                        dynamicButtonProp = False

                    if line.strip().lower().startswith("type "):
                        if dynamicButton == True and len(constProp) > 0:
                            with open(outFile, "a") as f:
                                f.write("event constructor;call super::constructor;")
                                f.write("\n")
                                for setter in constProp:
                                    f.write(setter)
                                    f.write("\n")
                                f.write("end event")
                                constProp = {""}
                                dynamicButton = False
                                f.write("\n")
                                f.write("\n")

                    if " from u_dynamic_button within " in line.lower():
                        dynamicButton = True
                        dynamicButtonProp = True
                    elif line.strip().lower().startswith("type cb_") or  line.strip().lower().startswith("type pb_"):
                        if "`" in line.lower():
                            dynamicButton = True
                            dynamicButtonProp = True
                    
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

                    if "end type" in line.lower():
                        dynamicButtonProp = False
                
                    if not skipLine:
                        with open(outFile, "a") as f:
                            insertSetter = False
                            insertConst = False
                            if dynamicButton == True:
                                if " event " in line.lower() and "constructor" in line.lower():
                                    insertSetter = True
                            
                            if insertSetter == True:
                                f.write(line.rstrip())
                                f.write("\n")
                                for settter in constProp:
                                    f.write(settter)
                                    f.write("\n")
                                constProp.clear()
                            else:
                                f.write(line.rstrip())
                                f.write("\n")
                    skipLine = False
                
                for setter in constProp:
                    if setter == "this.resize_inner_objects(this.width, this.height)":
                        with open(outFile, "a") as f:
                            f.write("event constructor;call super::constructor;")
                            f.write("\n")
                            for setter in constProp:
                                f.write(setter)
                                f.write("\n")
                            constProp.clear()

                            f.write("end event")
                            f.write("\n")

