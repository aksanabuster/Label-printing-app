import os
#test.html
import imgkit

class Printer:
    def __init__(self,name,status):
        self.printerName = name
        self.status = status

    def print(self, fileUri, outputname='badge-test',fileType = 'png'):
        if self.status == 'disabled':
            print("This printer status must be 'enabled' to print (cupsenable *printerName*).")
            return
        
        filename = "{}.{}".format(outputname, fileType)
        # Formatting
        options = {
            'format': fileType,
            'encoding': "UTF-8",

        }
        # Read-in url converts it to an IMAGE
        imgkit.from_url(fileUri,filename , options=options)
        # Returns new path of appended file
        # list_of_files = glob.glob('/home/boris/Documents/PrinterHub/' + str(filename))
        # latest_file_path = max(list_of_files, key=os.path.getctime)
        # print (latest_file_path)
        # Prints desired screenshot
        print(filename)
#        os.system("lp -P LabelPrinter-1 TEST.txt")
        command = "lp -d {} {}".format(self.printerName, filename)
        os.system(command)
        
        #os.system("lp -d %s %s" % self.printerName % filename)