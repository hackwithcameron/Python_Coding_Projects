from tkinter import *
import tkinter as tk
import os
from tkinter import filedialog

import directory_main
import directory_gui

#  Center window
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    center = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return center

def print_dir(self):
    path = findPath(self)
    self.txt_file.delete(0, END)
    self.txt_file.insert(0, path)


def findPath(self):
    sourcePath = filedialog.askdirectory()
    source = sourcePath
    return source



if __name__ == "__main__":
    pass