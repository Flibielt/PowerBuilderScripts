import codecs
import os

for root, dirs, files in os.walk(".\\", topdown=False):
   for name in files:
      if name.startswith("w_") or name.startswith("u"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "out" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)
        dynamicButton = False
        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:
                if "from u_dynamic_button" in line:
                    dynamicButton = True
                if "`" in line:
                    # cb: CommandButton
                    # pb: PictureButton
                    if "type cb_" in line or "type pb_" in line:
                        dynamicButton = True
                if dynamicButton == True:
                    if line.strip().startswith("event") and "clicked" in line and "doubleclicked" not in line:
                       line = line.replace("clicked", "u_click")
                       dynamicButton = False
                    if line.strip().startswith("event") and "ue_postclicked" in line:
                        line = line.replace("ue_postclicked", "u_click")
                        dynamicButton = False
                if "u_dynamic_button2" in line:
                    line = line.replace("u_dynamic_button2", "u_dynamic_button")
                
                if ".of_init_pbuo" in line.lower():
                    line = "//" + line
                
                if ".textsize" in line.lower() and "=" in line:
                    if "pb_" in line or "cb_" in line:
                        line = line.lower.lower().replace(".textsize", ".set_textsize(")
                        line = line.replace.replace("=", "")
                        line = line.rstrip() + ")"
                
                if " cb_" in line.lower() or " pb_" in line.lower():
                    if ".event" in line.lower() and "clicked()" in line.lower():
                        line = line.lower().replace("clicked()", "u_click(1, 1, 1)")

                with open(outFile, "a") as f:
                    f.write(line.rstrip())
                    f.write("\n")