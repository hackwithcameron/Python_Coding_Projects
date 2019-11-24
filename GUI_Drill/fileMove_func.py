from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
import sqlite3
import shutil
import time


import fileMove_main
import fileMove_gui

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo

#================================================
# DATABASES

def create_db(self):
    conn = sqlite3.connect("fileTransferRecords.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_transferTimes( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT, \
            col_time TEXT)")
        conn.commit()
    conn.close()



def recordMove(self):
    times, files = export(self)
    for x, y in zip(files, times):
        print("{} was last modified on {}...".format(x, time.asctime(y)))
    conn = sqlite3.connect("fileTransferRecords.db")
    with conn:
        cur = conn.cursor()
        for i, e in zip(files, times):
            try: # Checks for existing file in db if file already in db it does not get duplicated
                cur.execute("""SELECT col_file FROM tbl_transferTimes WHERE col_file = (?)""", [i])
                var = cur.fetchall()[0]
                if var[0] != i:
                    cur.execute("""INSERT INTO tbl_transferTimes(col_file, col_time) VALUES (?, ?)""", (i, time.asctime(e)))
                    print(var)
            except IndexError:
                cur.execute("""INSERT INTO tbl_transferTimes(col_file, col_time) VALUES (?, ?)""", (i, time.asctime(e)))
    conn.commit()
    conn.close()


#================================================

# From Path
def from_path(self):  # linked to "FROM" button
    fromPath = findPath(self)
    self.txt_from.delete(0, END)
    self.txt_from.insert(0, fromPath)

# To Path
def to_path(self):  # linked to "TO" button
    toPath = findPath(self)
    self.txt_to.delete(0, END)
    self.txt_to.insert(0, toPath)


# Function to find initial pathway for file
def findPath(self):
    sourcePath = filedialog.askdirectory()
    source = sourcePath
    return source

#================================================

# File move
def export(self):
    fromPath = self.txt_from.get()
    toPath = self.txt_to.get()
    times = []
    files = []
    dir = os.listdir(fromPath)
    try:
        for file in dir:
            if file[-1:-4:-1] == "txt":
                files.append(file)
    except FileNotFoundError:
        print("Directory or Files not found")
    for i in files:
        abPathFrom = os.path.join(fromPath, i)
        abPathTo = os.path.join(toPath, i)
        shutil.move(abPathFrom, abPathTo)
        moveTime = os.path.getmtime(abPathTo)
        times.append(time.localtime(moveTime))
    return times, files






if __name__ == "__main__":
    pass