from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root=Tk()
root.title("Google Translator prototype_1.0")
root.geometry("1000x400")
root.config(bg = '#F2CCC3')

title_label = Label(root, text = "Language Translator", bg='F2CCC3', font=("Sylfaen",18,"bold","italic"))
title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

input_label = Label(root, text = "Enter Text", bg='F2CCC3', font='arial 13 bold')
input_label.place(relx=0.02,rely=0.2,anchor=W)

Input_text = Label(root, bg='FFFCF9', font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60, bd=0)
Input_text.place(relx=0.02,rely=0.5,anchor=W)

root.mainloop()
