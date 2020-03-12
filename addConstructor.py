import codecs
import os

for root, dirs, files in os.walk("folderName", topdown=False):
   for name in files:
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "folderName_out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        if name.startswith("w_") or name.startswith("uov_") or name.startswith("u_"):
            lastLine = ""
            props = {""}
            button = False
            skipLine = False
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    skipLine = False

                    if button:
                        if "integer textsize" in line.lower() or "int textsize" in line.lower():
                            props.add("this.set_textsize(" + line[line.find("=") + 1:].strip() + ")")
                            skipLine = True
                        elif "string powertiptext" in line.lower():
                            props.add("this.add_powertip(" + line[line.find("=") + 1:].strip() + ")")
                            skipLine = True
                        elif "string text" in line.lower():
                            props.add("this.set_text(" + line[line.find("=") + 1:].strip() + ")")
                            skipLine = True
                        elif "string tag" in line.lower():
                            props.add("this.set_tag(" + line[line.find("=") + 1:].strip() + ")")
                            skipLine = True
                        elif "boolean default" in line.lower():
                            props.add("this.set_default(" + line[line.find("=") + 1:].strip() + ")")
                            skipLine = True
                        elif "boolean cancel" in line.lower():
                            props.add("this.set_cancel(" + line[line.find("=") + 1:].strip() + ")")
                            skipLine = True

                        if "constructor" in lastLine.lower() and ";" in line:
                            if len(props) > 0:
                                with open(outFile, "a") as fOut:
                                    for setter in props:
                                        fOut.write(setter)
                                        fOut.write("\n")
                                props.clear()
                                button = False
                        elif "type" in line and " from " in line:
                            if len(props) > 0:
                                validSetters = False
                                for setter in props:
                                    if len(setter) > 5:
                                        validSetters = True
                                if validSetters:
                                    with open(outFile, "a") as fOut:
                                        fOut.write("event constructor;call super::constructor;")
                                        fOut.write("\n")
                                        for setter in props:
                                            fOut.write(setter)
                                            fOut.write("\n")
                                        fOut.write("end event")
                                        fOut.write("\n")
                                        fOut.write("\n")
                            
                            props.clear()
                            button = False

                    if "from u_dynamic_button" in line:
                        button = True
                        props.add("this.resize_inner_objects(this.width, this.height)")
                    elif "end type" in line and "from u_dynamic_button" in lastLine:
                        props.clear()
                        button = False
                    elif "type cb_" in line or "type pb_" in line:
                        if "`cb_" in line or "`pb_" in line:
                            button = True
                            props.add("this.resize_inner_objects(this.width, this.height)")
                        
                    lastLine = line

                    if not skipLine:
                        with open(outFile, "a") as fOut:
                            fOut.write(line.rstrip())
                            fOut.write("\n")
            
            if len(props) > 0 and button:
                isValid = False
                for setter in props:
                    if len(setter) > 5:
                        isValid = True
                
                with open(outFile, "a") as fOut:
                    fOut.write("event constructor;call super::constructor;")
                    fOut.write("\n")
                    for setter in props:
                        fOut.write(setter)
                        fOut.write("\n")
                    fOut.write("end event")
                    fOut.write("\n")
                    fOut.write("\n")
                    