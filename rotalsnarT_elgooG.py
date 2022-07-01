from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root=Tk()
root.title("Google Translator prototype_1.0")
root.geometry("1000x400")
root.config(bg = '#F2CCC3')

language = list(LANGUAGE.values())
title_label = Label(root, text = "Language Translator", bg='F2CCC3', font=("Sylfaen",18,"bold","italic"))
title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

input_label = Label(root, text = "Enter Text", bg='F2CCC3', font='arial 13 bold')
input_label.place(relx=0.02,rely=0.2,anchor=W)
src_lang = ttk.Combobox(root, values = language, width = 22, state="readonly")
src_lang.place(relx=0.13,rely=0.2,anchor=W)
src_lang('English')

output_label = Label(root, text = "Output", bg='F2CCC3', font='arial 13 bold',)
output_label.place(relx=0.81,rely=0.5,anchor=E)
dest_lang = ttk.Combobox(root, values = language, width = 22, state="readonly")
dest_lang.place(relx=0.98,rely=0.2,anchor=E)
dest_lang.set('Choose Output Language')

Input_text = Label(root, bg='FFFCF9', font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60, bd=0)
Input_text.place(relx=0.02,rely=0.5,anchor=W)
Output_text = Label(root, bg='FFFCF9', font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60, bd=0)
Output_text.place(relx=0.98,rely=0.5,anchor=E)

def Translate():
    translator=Translator()
    try:
        translated=translator.translate(text= Input_text.get(1.0,END), src = src_lang.get(), dest = dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
    except:
        print("Try Again")
        

trans_btn = 
trans_btn.place(relx=0.098,rely=0.5,anchor=CENTER)
footer_label = 
footer_label.place(relx=0.098,rely=0.5,anchor=CENETR)
root.mainloop()
