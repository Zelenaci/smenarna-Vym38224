#sr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import *

# from tkinter import ttk


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárna"

    def __init__(self):
        super().__init__(className=self.name)
        v = tk.IntVar(self)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna", borderwidth=14)
        self.lbl.pack()
        self.lbl1 = tk.Label(self, text="Transakce")
        self.lbl1.pack(anchor=W)
        self.radiobutton1 = Radiobutton(self, text="Nákup", variable=v, value=1).pack(anchor=W)
        self.radiobutton2 = Radiobutton(self, text="Prodej", variable=v, value=2).pack(anchor=W)
        self.lbl1 = tk.Label(self, text="Měna")
        self.lbl1.pack(anchor=W)
        self.listbox = Listbox(self)
        self.listbox.insert(END,Měna)
        for item in [u"EUR", u"GBP", u"USD", u"JPY", u"IDR"]
        self.listbox.insert(END, item)

        self.lbl1 = tk.Label(self, text="Kurz")
        self.lbl1.pack(anchor=W)
        self.bind("<Escape>", self.quit)
        #quit
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()