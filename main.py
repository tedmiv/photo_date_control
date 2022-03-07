"""
The program to automatic synchronize EXIF date data and filename
"""

import tkinter as tk
from tkinter.filedialog import askdirectory
from os import listdir
from os.path import isfile, join
from exif import Image

window = tk.Tk()
window.withdraw()
directoryName = askdirectory(title="Choose the directory with photo files for \
    change", initialdir="/")
print(directoryName)
dirItems = listdir(directoryName)
files = list()
for file in dirItems:
    if isfile(join(directoryName, file)):
        fileExtension = file.split('.')
        if fileExtension[-1].lower() == "jpg":
            files.append(file)
print(files)

print('Ok')

window.mainloop()