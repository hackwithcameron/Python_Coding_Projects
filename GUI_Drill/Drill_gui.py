from tkinter import *
import tkinter as tk


import GUI_Drill.Drill_func as drill_func
import GUI_Drill.Drill_main as drill_main


def load_gui(self):

    #  Input bars
    self.txt_browse1 = tk.Entry(self.master, text="", width=40)
    self.txt_browse1.grid(row=0, column=1, columnspan=3, padx=(30, 0), pady=(40, 0), sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master, text="")
    self.txt_browse2.grid(row=1, column=1, columnspan=3, padx=(30, 0), pady=(10, 0), sticky=N+E+W)

    

    #  Buttons
    self.btn_browse1 = tk.Button(self.master, width=12, height=2, text="Browse...")
    self.btn_browse1.grid(row=0, column=0, padx=(15, 0), pady=(40, 0), sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=12, height=2, text="Browse...")
    self.btn_browse2.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky=W)
    self.btn_check = tk.Button(self.master, width=12, height=3, text="Check for files...")
    self.btn_check.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky=W+S)
    self.btn_close = tk.Button(self.master, width=12, height=3, text="Close Program")
    self.btn_close.grid(row=2, column=3, padx=(15, 0), pady=(0, 0), sticky=S+E)




 
