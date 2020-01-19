import tkinter as tk  # used for the GUI
from tkinter import filedialog
import os

root = tk.Tk()
apps = []

# removes contents of previous file
if os.path.isfile('double_chrome.txt'):
    with open('double_chrome.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


# function to make the button actually do something
def addApp():
    # stops it from displaying the same file name twice when a second is selected
    for widget in frame.winfo_children():
        widget.destroy()
    # opens file explorer and displays only executable files
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    # displays the chosen file
    for app in apps:
        label = tk.Label(frame, text=app, bg="red")
        label.pack()


# runs the apps
def runApps():
    for app in apps:
        os.startfile(app)


# canvas will make the window start bigger, and the bg will change the color
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# attaches it to root
canvas.pack()

# frame makes a container inside the window
frame = tk.Frame(root, bg="turquoise")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)  # relx and rely changes position of the white frame

# create the buttons
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

# add a delete button?

# displays the saved apps
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# saves the apps that were run into a file
with open('double_chrome.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
