import sys
from printer import Printer

debug = True

if debug == False:
    p = Printer("LabelPrinter-1")
    p.print("http://172.16.10.53:8888/gen/badge?fullname=Aksana&title=dude&co=blah","badge-test","png")

elif debug == True:
    p1 = Printer("LabelPrinter-2", 'enabled')
    p1.print("file:///home/pi/Documents/PrinterHub/test.html","badge-test","png")
    
    
