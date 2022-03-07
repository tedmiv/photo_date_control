"""
The program to automatic synchronize EXIF date data and filename
"""

import tkinter as tk
from tkinter.filedialog import askdirectory
from os import listdir, mkdir
from os.path import isfile, join
from exif import Image

window = tk.Tk()
window.withdraw()
directory_name = askdirectory(title="Choose the directory with photo files for \
    change", initialdir="/")
print(directory_name)
dir_items = listdir(directory_name)
files = list()
for file in dir_items:
    if isfile(join(directory_name, file)):
        file_extension = file.split('.')
        if file_extension[-1].lower() == "jpg":
            files.append(file)
print(files)

renamed_file_flag = False
with open(directory_name + '/' + files[1], 'rb') as original_file:
    file_to_check = Image(original_file)
if file_to_check.has_exif:
    print(file_to_check.datetime_original)
    exif_date_time = file_to_check.datetime_original
    if exif_date_time:
        if not renamed_file_flag:
            mkdir(directory_name + '/' + 'renamed_file')
            renamed_file_flag = True
        new_file_name = exif_date_time[0:4] + exif_date_time[5:7] \
            + exif_date_time[8:10] + '_' + exif_date_time[11:13] \
            + exif_date_time[14:16] + exif_date_time[17:]
        print(new_file_name)
        with open(directory_name + '/' + 'renamed_file' + '/' \
            + new_file_name + '.jpg', 'wb') as new_file:
            pass
        new_file.close()
original_file.close()

print('Ok')

window.mainloop()