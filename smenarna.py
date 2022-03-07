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
        v1 = tk.IntVar(self)
        v2 = tk.IntVar(self)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna", borderwidth=14)
        self.lbl.pack()

        #Transakce
        self.lbl1 = tk.Label(self, text="Transakce:")
        self.lbl1.pack(anchor=W)
        self.radiobutton1 = Radiobutton(self, text="Nákup", variable=v1, value=1).pack(anchor=W)
        self.radiobutton2 = Radiobutton(self, text="Prodej", variable=v1, value=2).pack(anchor=W)

        #Měna
        self.lbl2 = tk.Label(self, text="Měna:")
        self.lbl2.pack(anchor=W)
        self.listbox = Listbox(self)
        self.listbox.pack(anchor=W)
        self.listbox.bind("<ButtonRelease-1>", self.kliknu)
        
        f = open('listek.txt')
        self.radky = f.readlines()

        for radek in self.radky:
            radek = radek.split()
            self.listbox.insert(END, radek[0])

        #Kurz
        self.lbl3 = tk.Label(self, text="Kurz:")
        self.lbl3.pack(anchor=W)
        self.amount = tk.IntVar()
        self.price = tk.IntVar()
        self.vysledek = tk.IntVar()
        self.amountLbl= tk.Label(self, textvariable= self.amount) 
        self.amountLbl.pack()
        self.priceLbl= tk.Label(self, textvariable= self.price) 
        self.priceLbl.pack()
    


       
        #Výpočet
        self.lbl2 = tk.Label(self, text="Výpočet:")
        self.lbl2.pack(anchor=W)
        self.entry1 = tk.Entry(self)
        self.entry1.pack()
        self.btn2 = tk.Button(self, text="Výpočet", command=self.vypocet)
        self.btn2.pack(anchor=E)
        self.lbl3 = tl.Label(self, text="")
        self.lbl3.pack(anchor=W))

        #Quit
        self.bind("<Escape>", self.quit)
        self.btn1 = tk.Button(self, text="Quit", command=self.quit)
        self.btn1.pack()

        

    def vypocet(self):  
        e = self.entry.get()
        a = self.amount.get()
        p = self.price.get()
        self.vysledekVar = round(e*p/a)
        self.vysledek.set(self.vysledekVar)

    
    def kliknu(self, event):
        index = self.listbox.curselection()[0]
        f = open("listek.txt")
        self.lines = f.readlines()
        self.amountVar = self.lines[index].split()[1]
        self.amount.set(self.amountVar)
        self.priceVar = self.lines[index].split()[2] 
        self.price.set(self.priceVar)
        print(self.radky[index])


          
        
        
        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()