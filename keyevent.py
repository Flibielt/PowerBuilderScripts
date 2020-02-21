import codecs
import os

buttons = {""}

for root, dirs, files in os.walk("..\\medikai", topdown=False):
   for name in files:
      if name.startswith("w_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "..\\out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_dynamic_button within" in line:
                    buttons.add(line[line.find("type ") + 4:line.find(" from")].strip())
        
        with codecs.open(fileName, encoding='utf8') as f:
            endCount = 0
            for line in f:
                with open(outFile, "a") as f:
                    if "end on" in line:
                        endCount = endCount + 1
                    elif endCount == 2:
                        f.write("event key;IF keyflags = 0 THEN\n")
                        f.write("	IF key = KeyEscape! THEN\n")
                        for button in buttons:
                            f.write("		" + button + ".event post u_click(5, 1, 1)\n")
                        f.write("	ELSEIF key = KeyEnter! THEN\n")
                        for button in buttons:
                            f.write("		" + buttons + ".event post u_click(6, 1, 1)\n")
                        f.write("	END IF\n")
                        f.write("END IF\n")
                        f.write("end event\n")
                        endCount = 3
                        f.write(line.rstrip())
                        f.write("\n")
                    else:
                        f.write(line.rstrip())
                        f.write("\n")
                    
