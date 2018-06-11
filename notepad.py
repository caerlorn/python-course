import Tkinter as tiki
import tkFileDialog
import tkMessageBox
from ScrolledText import *


motherContainer = tiki.Tk(className=" Poor man's notepad")
motherContainer.minsize(width=300,height=200)
textFrame = ScrolledText(motherContainer, wrap="word", width=60, height=30, font=("Consolas", 11), undo=True)
textFrame.pack(fill="both", expand=True)


# CTRL+a was not working because it seems the default shortcut is Ctrl + / for select all in tkinter so I will rebind it
def selectAll(event):
    textFrame.tag_add(tiki.SEL, "1.0", tiki.END)
    textFrame.mark_set(tiki.INSERT, "1.0")
    textFrame.see(tiki.INSERT)
    return 'break'
    pass


def openFile():
    data = tkFileDialog.askopenfile(parent=motherContainer, mode="rb", title="Please select a file")
    if data is not None:
        contents = data.read()
        textFrame.delete('1.0', tiki.END)
        textFrame.insert('1.0', contents)
        data.close()
    pass


def saveFile():
    contents = textFrame.get('1.0', tiki.END)
    data = tkFileDialog.asksaveasfile(mode='w', title="Save file", defaultextension='.txt',
                                      filetypes=(("Text Documents", "*.txt"), ("All Files", "*.*")))
    if data:
        data.write(contents)
        data.close()
    pass


def help():
    tkMessageBox.showinfo("About", "Version: 0.1 \nPython Homework 3\nAuthor: "
                          "Yildirim Can Sehirlioglu\nStudent ID: 156336IVCM")
    pass


textFrame.bind("<Control-Key-a>", selectAll)
textFrame.bind("<Control-Key-A>", selectAll)
mainMenu = tiki.Menu(motherContainer)
motherContainer.config(menu=mainMenu)
flMenu = tiki.Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="File", menu=flMenu)
flMenu.add_command(label="Open", command=openFile)
flMenu.add_command(label="Save", command=saveFile)
flMenu.add_separator()
flMenu.add_command(label="Close", command=motherContainer.quit)
mainMenu.add_command(label="Help", command=help)
motherContainer.mainloop()
