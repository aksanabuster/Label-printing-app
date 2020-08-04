import glob
import os

image = 

list_of_files = glob.glob('/home/boris/Documents/PrinterHub/%s') % image
latest_file_path = max(list_of_files, key=os.path.getctime)
print (latest_file_path)