# Python Ver:   3.7.2
#
# Purpose:      Phonebook GUI using Tkinter Parent and Child relationship
#               Tech Academy Demo
#
#
# Tested OS:    macOS 10.13

from tkinter import *
import tkinter as tk


from GUI_Drill import Drill_func as drill_func
from GUI_Drill import Drill_gui as drill_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)



        #  Configuration of window
        self.master = master
        self.master.minsize(550, 200)
        self.master.maxsize(550, 200)
        drill_func.center_window(self, 550, 200)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        

        drill_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

