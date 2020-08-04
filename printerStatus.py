import os
from printer import Printer

#printers = ['LabelPrinter-0', 'LabelPrinter-1', 'LabelPrinter-2', 'LabelPrinter-3', 'LabelPrinter-4']

printers = []

checkIfIdle = "lpstat -p"
macAddy = "cat /sys/class/net/wlan0/address"

def getPrinters():
    output = os.popen(checkIfIdle).read()

    lines = output.split("\n")
    lines.pop(-1)
    
    for l in lines:
        parts = l.split(' ')
        # print(parts[0])
        if parts[0] != 'printer':
            lines.remove(l)
    # print(lines)

    for l in lines:
        parts = l.split(' ')
        # index 1 = printer name, index 3 = status
        printerName = parts[1]
        printerStatus = parts[parts.index('since')-1]
        print("{}: {}".format(printerName,printerStatus))
        printers.append(Printer(printerName, printerStatus))
        
    #print(printers)
    return printers
    
    # for p in printers:
    #     p.print("file:///home/boris/Documents/PrinterHub/test.html","badge-test","png")
    
        
def getMAC():
    os.system(macAddy)



#getPrinters()
#print("Mac Address:",getMAC())
