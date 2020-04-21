class PathManeger:
    def read_paths(self):
        import os
        file = open('C:\\Users\\Aleksander\\PycharmProjects\\scripts\\paths.txt', 'r')
        lines = file.read().split('\n')
        file.close()
        return lines

    def new_path(self):
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()

        dir_path = filedialog.askdirectory()
        self.append_path(dir_path)
        pass

    def append_path(self, dir_path):
        file = open('paths.txt', 'a')
        file.write(dir_path+'\n')
        file.close()
        pass

