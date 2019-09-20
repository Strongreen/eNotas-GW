import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  

import 

# Janela

jan = Tk()
jan.title("Emitindo notas via planilha")
jan.geometry("900x400")
jan.configure(background="white")
jan.resizable(width=False, height=False)


# Widgets

RightFrame = Frame(jan, width=900, height=400, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

PathLabel = Label(RightFrame, text="Caminho: ", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
PathLabel.place(x=50,y=60)

PathEntry = ttk.Entry(RightFrame,width=100)
PathEntry.place(x=200,y=70)

APILabel = Label(RightFrame, text="API Key: ", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
APILabel.place(x=30,y=180)

APIEntry = ttk.Entry(RightFrame,width=100)
APIEntry.place(x=200,y=180)

IDEmpresaLabel = Label(RightFrame, text="ID da Empresa: ", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
IDEmpresaLabel.place(x=0,y=280)

IDEmpresaEntry = ttk.Entry(RightFrame,width=100)
IDEmpresaEntry.place(x=200,y=290)

# Botoes

EmitirButton = ttk.Button(RightFrame,text="Emitir as Notas", width=30)
EmitirButton.place(x=300,y=350)


jan.mainloop()