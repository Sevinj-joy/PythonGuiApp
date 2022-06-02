from fileinput import filename
import tkinter as tk
from tkinter import *
from tkinter import Canvas, filedialog, Text
import os

from click import open_file

root=tk.Tk()
apps=[]

def addApp():
    filename=filedialog.askopenfilename(initialdir="/", title="Select File" , 
    filetypes=(("executable", "*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApp():
   for app in apps:
       os.startfile(app)


canvas=tk.Canvas(root, height=500, width=700, bg="#263D42")
canvas.pack()

frame =tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile=tk.Button(root, text="Open File", padx=10,
                 pady=5, fg="white", bg="#263D42", command = addApp)
openFile.pack(side="top")

runApps=tk.Button(root, text="Run Apps", padx=10,
                 pady=5, fg="white", bg="#263D42",command = runApp)
runApps.pack(side="top")

root.mainloop()
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app+ ",")
