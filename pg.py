from tkinter import *
from tkinter import messagebox
import random

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '#', '$','&']


    if len(numbers_entry.get())!=0 and len(letters_entry.get())!=0 and len(symbols_entry.get())!=0:
        password_list = []
        nr_numbers = int(numbers_entry.get())
        nr_letters = int(letters_entry.get())
        nr_symbols = int(symbols_entry.get())
        for char in range(nr_letters):
          password_list.append(random.choice(letters))

        for char in range(nr_symbols):
          password_list += random.choice(symbols)

        for char in range(nr_numbers):
          password_list += random.choice(numbers)

        random.shuffle(password_list)

        password = ""
        for char in password_list:
          password += char
        password_entry.insert(0,password)
        messagebox.showinfo(title='CONFIRMATION',message="Password generated successfully !!")
    else:
        messagebox.showerror(title='ATTENTION',message='Fill all required entrys !!')


window=Tk()
window.geometry('400x400')
window.title("Passward Generator")

#*********Canvas********

canvas=Canvas(window)
canvas.place(x=130,y=0)
img=PhotoImage(file="logo.png")
canvas.create_image(70,85,image=img)

#***********label***************

nr_letters =Label(text="Letters :")
nr_letters.place(x=120,y=240,width=50)
nr_symbols = Label(text="Symbols :")
nr_symbols.place(x=120,y=280,width=50)
nr_numbers = Label(text="Digits :")
nr_numbers.place(x=120,y=320,width=50)

#***********Entry*********

letters_entry=Entry(width=15)
letters_entry.place(x=175,y=240)
symbols_entry=Entry(width=15)
symbols_entry.place(x=175,y=280)
numbers_entry=Entry(width=15)
numbers_entry.place(x=175,y=320)
password_entry=Entry(width=30)
password_entry.place(x=115,y=200,height=20)

#***********Button*********

generate=Button(window,text='GENERATE',bg='green',command=generate_pass)
generate.place(x=175,y=350,height=25,width=92)

window.mainloop()