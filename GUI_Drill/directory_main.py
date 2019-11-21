# Python Ver:   3.7
#
# Purpose:      Show user directory path
#
#
#
# Tested OS:    macOS 10.13

from tkinter import *
import tkinter as tk


import directory_func
import directory_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)



        #  Configuration of window
        self.master = master
        self.master.minsize(500, 150)
        self.master.maxsize(500, 150)
        directory_func.center_window(self, 500, 150)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")


        directory_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

