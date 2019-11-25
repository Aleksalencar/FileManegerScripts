import tkinter
from tkinter import messagebox
from tkinter import filedialog

main_win = tkinter.Tk()
main_win.geometry("1000x500")
main_win.sourceFolder = ''
main_win.sourceFile = ''
def chooseDir():
    main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Please select a directory')

b_chooseDir = tkinter.Button(main_win, text = "Chose Folder", width = 20, height = 3, command = chooseDir)
b_chooseDir.place(x = 50,y = 50)
b_chooseDir.width = 100


def chooseFile():
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a directory')

b_chooseFile = tkinter.Button(main_win, text = "Chose File", width = 20, height = 3, command = chooseFile)
b_chooseFile.place(x = 250,y = 50)
b_chooseFile.width = 100

main_win.mainloop()
print(main_win.sourceFolder)
print(main_win.sourceFile )