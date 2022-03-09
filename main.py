"""
The program to automatic synchronize EXIF date data and filename
"""

import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning, showinfo
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

renamed_file_flag = False
previous_new_file_name = str()
new_file_name_digit = 1
renamed_files_quantity = 0
for i in range(len(files)):
    with open(directory_name + '/' + files[i], 'rb') as original_file:
        file_to_check = Image(original_file)
        original_file.close()
    if file_to_check.has_exif:
        print(file_to_check.datetime_original)
        exif_date_time = file_to_check.datetime_original
        if exif_date_time:
            if not renamed_file_flag:
                if 'renamed_file' in dir_items:
                    showwarning(title='Warning!', \
                        message='Folder "renamed_file" is already exists')
                    quit()
                else:
                    mkdir(directory_name + '/' + 'renamed_file')
                renamed_file_flag = True
            new_file_name = exif_date_time[0:4] + exif_date_time[5:7] \
                + exif_date_time[8:10] + '_' + exif_date_time[11:13] \
                + exif_date_time[14:16] + exif_date_time[17:]
            temp_new_file_name = new_file_name
            if previous_new_file_name == new_file_name:
                new_file_name = new_file_name + '_' + str(new_file_name_digit)
                new_file_name_digit += 1
            else:
                new_file_name_digit = 1
            previous_new_file_name = temp_new_file_name
            with open(directory_name + '/' + 'renamed_file' + '/' \
                + new_file_name + '.jpg', 'wb') as new_file, \
                open(directory_name + '/' + files[i], 'rb') as original_file:
                #buffer = original_file.read()
                new_file.write(original_file.read())
                print(files[i] + ' - ' + new_file_name + '.jpg')
                renamed_files_quantity += 1
                new_file.close()
                original_file.close()

showinfo_message = 'All files quantity - ' + str(len(files)) + \
    '\nRenamed files quantity - ' + str(renamed_files_quantity)
print(showinfo_message)
showinfo(title='Program had done!', message=showinfo_message)

window.mainloop()