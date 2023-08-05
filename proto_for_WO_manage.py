import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk

root = tk.Tk()
file_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTOZPXrV1XqR344xWaWpbfYz72eh_rLH1U1qWWClyy6yI246H9tC_24JBr2Z6hoVrJWTNJuaqE_bxmN/pub?output=xlsx'
xcl = pd.ExcelFile(file_url)
zero_button = tk.Button(root, text='0', fg='black', bg='yellow')
zero_button.grid(column=0,row=0, padx='5px', pady="15px")
zero_text = tk.Label(root, text="0.Update all days", fg='purple')
zero_text.grid(column=1, row=0, padx='5px')
buttons_for_sheets = []
sheets = []
for num, sheet in enumerate(xcl.sheet_names):
    buttons_for_sheets.append(None)
    buttons_for_sheets[num] = tk.Button(root, text=f'{num+1}', fg="black", bg='yellow')
    buttons_for_sheets[num].grid(column=0, row=num+1, padx='5px', pady="15px")

    sheets.append(None)
    sheets[num] = tk.Label(root,text=f"{num + 1}.Update {num + 1} day ({sheet})", fg='purple')
    sheets[num].grid(column=1, row=num+1, padx='5px', sticky=tk.E)
exit_button= tk.Button(root, text="EXIT",fg='black', bg='red')
exit_button.grid(column=1,row=(len(xcl.sheet_names)+1), padx='5px', pady="15px", sticky=tk.EW)

root.mainloop()
