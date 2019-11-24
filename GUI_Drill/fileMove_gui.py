from tkinter import *
import tkinter as tk

import fileMove_main
import fileMove_func


def load_gui(self):

    #  Labels
    self.lbl_from = tk.Label(self.master, text="Please Fill in all Fields above", bg="#F0F0F0")
    self.lbl_from.grid(row=3, column=1, padx=(0, 0), pady=(5, 5), sticky=N+W)


    #  Text Boxes
    self.txt_from = tk.Entry(self.master, text="From File...")
    self.txt_from.grid(row=0, column=1, rowspan=1, columnspan=2, padx=(0, 0), pady=(31, 0), sticky=N+E+W)
    self.txt_to = tk.Entry(self.master, text="To File...")
    self.txt_to.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(0, 0), pady=(31, 0), sticky=N+E+W)


    #  Buttons
    self.btn_from = tk.Button(self.master, text="From File...", width=12, height=2, command=lambda: fileMove_func.from_path(self))
    self.btn_from.grid(row=0, column=0, padx=(20, 0), pady=(25, 0), sticky=W)
    self.btn_to = tk.Button(self.master, text="To File...", width=12, height=2, command=lambda: fileMove_func.to_path(self))
    self.btn_to.grid(row=1, column=0, padx=(20, 0), pady=(25, 0), sticky=W)
    self.btn_export = tk.Button(self.master, text="Export", width=12, height=2, command=lambda: fileMove_func.recordMove(self))
    self.btn_export.grid(row=4, column=2, padx=(0, 0), pady=(0, 0), sticky=E)






if __name__ == "__main__":
    pass