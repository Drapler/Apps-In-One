import tkinter as tk
from tkinter import filedialog, scrolledtext
import os

root = tk.Tk()
root.resizable(False, False)
root.title("Apps In One")
root.iconbitmap(r'appinone.ico')
apps = []
file = "save.txt"
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#def myDelete():
    #file()

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                        filetypes=(("executables",".exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=300, width=400, bg="#5679D2")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.65, relx=0.1, rely=0.1)

openFile = tk.Button(root,text="Open File", padx=174,
                     pady=5, fg="white", bg="#5679D2", command=addApp)
openFile.pack()

runApps = tk.Button(root,text="Run  Apps", padx=172,
                     pady=5, fg="white", bg="#5679D2", command=runApps)
runApps.pack()

#DeleteButton = tk.Button(root,text="Delete Apps", padx=10,
                     #pady=5, fg="white", bg="#263D42", command=myDelete)
#DeleteButton.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
