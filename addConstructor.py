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
            with codecs.open(fileName, encoding='utf8') as f:
                for line in f:
                    if " from u_dynamic_button " in line:
                        button = True
                        props.add("this.resize_inner_objects(this.width, this.height)")
                    elif "end type" in line and " from u_dynamic_button " in lastLine:
                        props.clear()
                        button = False
                    elif button:
                        if "constructor" in lastLine.lower():
                            if len(props) > 0:
                                with open(outFile, "a") as fOut:
                                    for setter in props:
                                        fOut.write(setter)
                                        fOut.write("\n")
                                button = False
                        elif " type " in line and " from " in line:
                            if len(props) > 0:
                                with open(outFile, "a") as fOut:
                                    fOut.write("event constructor;call super::constructor;")
                                    fOut.write("\n")
                                    for setter in props:
                                        fOut.write(setter)
                                        fOut.write("\n")
                                    fOut.write("end event")
                                    fOut.write("\n")
                                    fOut.write("\n")
                    lastLine = line

                    with open(outFile, "a") as fOut:
                        fOut.write(line.rstrip)
                        fOut.write("\n")
                    