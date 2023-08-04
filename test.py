import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk

root = tk.Tk()
root.title("TESTING PRODUCT")
buttons = []
texts = []
text = tk.Label(text="LOL")

link_to_xcl = 'https://docs.google.com/spreadsheets/d/1b0plqR5RodygHOkzW2pEYDcle3SSPAS-0mcqIkvEljg/edit?usp=sharing'
xcl = pd.ExcelFile(link_to_xcl)

for i, name in enumerate(xcl.sheet_names):
    print(name, i)
def clicked():
    buttons[r].configure(fg='red')

for r in range(10):
    buttons.append(None)
    texts.append(None)
    buttons[r] = tk.Button(root, text=f'{r}', fg="red")
    texts[r] = tk.Label(root,text=f"This is line number {r}", fg='blue')
    buttons[r].grid(column=0, row=r,padx='5px', pady="15px")
    texts[r].grid(column=1, row=r,padx='5px')

text.grid()
root.mainloop()
