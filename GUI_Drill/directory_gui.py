from tkinter import *
import tkinter as tk

import directory_func
import directory_main


def load_gui(self):

    #  Text
    self.txt_file = tk.Entry(self.master, text="", width=50)
    self.txt_file.grid(row=0, column=0, padx=(18, 0), pady=(30, 0), sticky=N+E+W)

    #  Button
    self.btn_showPath = tk.Button(self.master, width=12, height=2, text="Choose File...", command=lambda: directory_func.print_dir(self))
    self.btn_showPath.grid(row=1, column=0, padx=(20, 0), pady=(10, 0), sticky=N)

