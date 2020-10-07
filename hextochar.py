import codecs
import os

for root, dirs, files in os.walk("map", topdown=False):
   for name in files:
      if name.startswith("d_"):
        fileName = os.path.join(root, name)
        print(fileName)
        outFile = "out4new" + fileName[fileName.find("\\"):]
        os.makedirs(os.path.dirname(outFile), exist_ok=True)

        with codecs.open(fileName, encoding='utf8') as f:
            for line in f:			
                if "$$HEX1$$e100$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$e100$$ENDHEX$$", u'\xe1'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$e100$$endhex$$", u'\xe1'.encode('cp1250').decode('cp1250'))
					
                if "$$HEX1$$e900$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$e900$$ENDHEX$$", u'\xe9'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$e900$$endhex$$", u'\xe9'.encode('cp1250').decode('cp1250'))

                if "$$HEX2$$e9002000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$e9002000$$ENDHEX$$", u'\xe9'.encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$e9002000$$endhex$$", u'\xe9'.encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$c900$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$c900$$ENDHEX$$", u'\xc9'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$c900$$endhex$$", u'\xc9'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$e1002000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$e1002000$$ENDHEX$$", u'\xe1'.encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex1$$e1002000$$endhex$$", u'\xe1'.encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$c100$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$c100$$ENDHEX$$", u'\xc1'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$c100$$endhex$$", u'\xc1'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$ed00$$ENDHEX$$".lower() in line.lower() or "$$hex2$$ed00ed00$$endhex$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$ed00$$ENDHEX$$", u'\xed'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$ed00$$endhex$$", u'\xed'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$$$HEX2$$ed00ed00$$ENDHEX$$", u'\xed'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex2$$ed00ed00$$endhex$$", u'\xed'.encode('cp1250').decode('cp1250'))

                if "$$HEX2$$ed002000$$ENDHEX$$".lower() in line:
                    line = line.replace("$$HEX2$$ed002000$$ENDHEX$$", u'\xed'.encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$ed002000$$endhex$$", u'\xed'.encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$cd00$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$cd00$$ENDHEX$$", u'\xcd'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$cd00$$endhex$$", u'\xcd'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$f600$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$f600$$ENDHEX$$", u'\xf6'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$f600$$endhex$$", u'\xf6'.encode('cp1250').decode('cp1250'))

                if "$$HEX2$$f6002000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$f6002000$$ENDHEX$$", u'\xf6'.encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$f6002000$$endhex$$", u'\xf6'.encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$d600$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$d600$$ENDHEX$$", u'\xd6'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$d600$$endhex$$", u'\xd6'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$5101$$ENDHEX$$".lower() in line.lower() or "$$hex1$$5001$$endhex$$" in line.lower():
                    line = line.replace("$$HEX1$$5101$$ENDHEX$$", u"\u0151".encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$5101$$endhex$$", u"\u0151".encode('cp1250').decode('cp1250'))
                    line = line.replace("$$HEX1$$5001$$ENDHEX$$", u"\u0151".encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$5001$$endhex$$", u"\u0151".encode('cp1250').decode('cp1250'))

                if "$$HEX2$$51012000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$51012000$$ENDHEX$$", u"\u0151".encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$51012000$$endhex$$", u"\u0151".encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$f300$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$f300$$ENDHEX$$", u'\xf3'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$f300$$endhex$$", u'\xf3'.encode('cp1250').decode('cp1250'))

                if "$$HEX2$$f3002000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$f3002000$$ENDHEX$$", u'\xf3'.encode('cp1250').decode('cp1250')  + ' ')
                    line = line.replace("$$hex2$$f3002000$$endhex$$", u'\xf3'.encode('cp1250').decode('cp1250')  + ' ')

                if "$$HEX1$$d300$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$d300$$ENDHEX$$", u'\xd3'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$d300$$endhex$$", u'\xd3'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$fa00$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$fa00$$ENDHEX$$", u'\xfa'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$fa00$$endhex$$", u'\xfa'.encode('cp1250').decode('cp1250'))

                if "$$HEX2$$fa002000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$fa002000$$ENDHEX$$", u'\xfa'.encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$fa002000$$endhex$$", u'\xfa'.encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$da00$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$da00$$ENDHEX$$", u'\xda'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$da00$$endhex$$", u'\xda'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$fc00$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$fc00$$ENDHEX$$", u'\xfc'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$fc00$$endhex$$", u'\xfc'.encode('cp1250').decode('cp1250'))

                if "$$HEX2$$fc002000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$fc002000$$ENDHEX$$", u'\xfc'.encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$fc002000$$endhex$$", u'\xfc'.encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$dc00$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$dc00$$ENDHEX$$", u'\xdc'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$dc00$$endhex$$", u'\xdc'.encode('cp1250').decode('cp1250'))
					
                if "$$hex2$$dc002000$$endhex$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$dc002000$$ENDHEX$$", u'\xdc'.encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$dc002000$$endhex$$", u'\xdc'.encode('cp1250').decode('cp1250') + ' ')

                if "$$HEX1$$b000$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$b000$$ENDHEX$$", u'\xb0'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$b000$$endhex$$", u'\xb0'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$b700$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$b700$$ENDHEX$$", u'\xff'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$b700$$endhex$$", u'\xff'.encode('cp1250').decode('cp1250'))

                if "$$HEX1$$b400$$ENDHEX$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$b400$$ENDHEX$$", u'\xb4'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$b400$$endhex$$", u'\xb4'.encode('cp1250').decode('cp1250'))
					
                if "$$hex1$$7101$$endhex$$".lower() in line.lower():
                    line = line.replace("$$HEX1$$7101$$ENDHEX$$", u'\u0171'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex1$$7101$$endhex$$", u'\u0171'.encode('cp1250').decode('cp1250'))
					
                if "$$hex3$$f3002000e100$$endhex$$".lower() in line.lower():
                    line = line.replace("$$HEX3$$f3002000e100$$ENDHEX$$", u'\xf3'.encode('cp1250').decode('cp1250') + ' ' + u'\xe1'.encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex3$$f3002000e100$$endhex$$", u'\xf3'.encode('cp1250').decode('cp1250') + ' ' + u'\xe1'.encode('cp1250').decode('cp1250'))
					
                if "$$hex2$$71012000$$endhex$$".lower() in line.lower():
                    line = line.replace("$$HEX2$$71012000$$ENDHEX$$", u"\u0171".encode('cp1250').decode('cp1250') + ' ')
                    line = line.replace("$$hex2$$71012s000$$endhex$$", u"\u0171".encode('cp1250').decode('cp1250') + ' ')
					
                if "$$hex4$$f3000d000a00d600$$endhex$$".lower() in line.lower():
                    line = line.replace("$$hex4$$f3000d000a00d600$$endhex$$", u"\xf3".encode('cp1250').decode('cp1250') + ' ' + u"\xf6".encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex4$$f3000d000a00d600$$endhex$$", u"\xf3".encode('cp1250').decode('cp1250') + ' ' + u"\xf6".encode('cp1250').decode('cp1250'))
					
                if "$$hex2$$e100ed00$$endhex$$".lower() in line.lower():					
                    line = line.replace("$$hex2$$e100ed00$$endhex$$", u"\xe1".encode('cp1250').decode('cp1250') + ' ' + u"\xed".encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex2$$e100ed00$$endhex$$", u"\xe1".encode('cp1250').decode('cp1250') + ' ' + u"\xed".encode('cp1250').decode('cp1250'))		
					
                if "$$hex3$$51012000e100$$endhex$$".lower() in line.lower():					
                    line = line.replace("$$hex3$$51012000e100$$endhex$$", u"\u0151".encode('cp1250').decode('cp1250') + ' ' + u"\xe1".encode('cp1250').decode('cp1250'))
                    line = line.replace("$$hex3$$51012000e100$$endhex$$", u"\u0151".encode('cp1250').decode('cp1250') + ' ' + u"\xe1".encode('cp1250').decode('cp1250'))		
					
                with open(outFile, "a") as f:
                    f.write(line.rstrip())
                    f.write("\n")