# Python Ver:   3.7
#
# Purpose:      Show user directory path
#
#
#
# Tested OS:    macOS 10.13

from tkinter import *
import tkinter as tk


import fileMove_func
import fileMove_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)



        #  Configuration of window
        self.master = master
        self.master.minsize(450, 200)
        self.master.maxsize(450, 200)
        fileMove_func.center_window(self, 450, 200)
        self.master.title("Export .txt Files")
        self.master.configure(bg="#F0F0F0")
        fileMove_func.create_db(self)


        fileMove_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

