import os
from tkinter import filedialog
import tkinter as tk

print(os.getcwd())
root = tk.Tk()
root.withdraw()
root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                           filetypes=[("Image Files", "*.jpg")])
print(root.filename)
