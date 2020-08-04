import os
#test.html
import imgkit
import glob

# Name of the screenshotted image
new_image = 'texttt.png'
# Formatting
options = {
    'format': 'png',
    'encoding': "UTF-8"
}
# Read-in url converts it to an IMAGE
imgkit.from_url('file:///home/pi/Documents/PrinterHub/test.html',new_image , options=options)
# Returns new path of appended file
list_of_files = glob.glob('/home/pi/Documents/PrinterHub/' + str(new_image))
latest_file_path = max(list_of_files, key=os.path.getctime)
print (latest_file_path)
# Prints desired screenshot
filename = new_image
os.system("lp %s" % filename)