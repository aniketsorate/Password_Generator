from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def division(a,b):
    if b!=0:
        return a/b
    else:
        return "errord"

def multiplication(a,b):
    return a * b

def modules(a,b):
    if b!=0:
        return a % b
    else:
        return "errorm"


def one():
    calsi.insert(END,1)
def two():
    calsi.insert(END, 2)
def three():
    calsi.insert(END, 3)
def four():
    calsi.insert(END, 4)
def five():
    calsi.insert(END, 5)
def six():
    calsi.insert(END, 6)
def seven():
    calsi.insert(END, 7)
def eight():
    calsi.insert(END, 8)
def nine():
    calsi.insert(END, 9)
def zero():
    calsi.insert(END, 0)
def plus():
    calsi.insert(END, '+')
def minus():
    calsi.insert(END, '-')
def multiply():
    calsi.insert(END, '*')
def divide():
    calsi.insert(END, '/')
def ac():
    calsi.delete(0,END)
def equal():

    string=calsi.get()
    print(string)
    operations=['+','-','*','/']
    for  i in string:
        if i in operations:
            result=0
            oper_index=string.index(i)
            a=int(string[:oper_index])
            b=int(string[oper_index+1:])
            if i == '+':
                result = add(a, b)
            elif i == '-':
                result = subtract(a, b)
            elif i == '*':
                result = multiplication(a, b)
            elif i == '/':
                result = division(a, b)

            if result != 'errord' and result != 'errorm':
                calsi.delete(0,END)
                calsi.insert(0, result)

            else:
                error = ''
                if result == 'errord':
                    error = 'Division'
                elif result == 'errorm':
                    error = 'Modules'
                messagebox.showerror(title='ATTENTION', message=f'{error} by zero is not possible')



window=Tk()
window.title("Simple Calculator")
window.geometry("400x400")
window.config(bg='#81D8D0')

#*********Frame**********

frame=Frame(window,height=320,width=300,bg='#FAF9F6')
frame.place(x=50,y=60)

# #********Label********

name=Label(text="CALCULATOR",fg='black',font=('times new roman',20,'bold'),bg='#81D8D0')
name.place(x=100,y=10)

#********Entry*********

calsi=Entry(frame )
calsi.place(x=30,y=40,width=240,height=40)

#*********Button*********

one=Button(frame,text='1',font=('times new roman',12,'bold'),command=one)
one.place(x=30,y=110,height=30,width=40)
two=Button(frame,text='2',font=('times new roman',12,'bold'),command= two)
two.place(x=90,y=110,height=30,width=40)
three=Button(frame,text='3',font=('times new roman',12,'bold'),command= three)
three.place(x=150,y=110,height=30,width=40)
four=Button(frame,text='4',font=('times new roman',12,'bold'),command=four)
four.place(x=30,y=160,height=30,width=40)
five=Button(frame,text='5',font=('times new roman',12,'bold'),command=five)
five.place(x=90,y=160,height=30,width=40)
six=Button(frame,text='6',font=('times new roman',12,'bold'),command=six)
six.place(x=150,y=160,height=30,width=40)
seven=Button(frame,text='7',font=('times new roman',12,'bold'),command=seven)
seven.place(x=30,y=210,height=30,width=40)
eight=Button(frame,text='8',font=('times new roman',12,'bold'),command=eight)
eight.place(x=90,y=210,height=30,width=40)
nine=Button(frame,text='9',font=('times new roman',12,'bold'),command=nine)
nine.place(x=150,y=210,height=30,width=40)
zero=Button(frame,text='0',font=('times new roman',12,'bold'),command=zero)
zero.place(x=90,y=260,height=30,width=40)
plus=Button(frame,text='+',font=('times new roman',12,'bold'),command= plus)
plus.place(x=210,y=110,height=30,width=40)
minus=Button(frame,text='-',font=('times new roman',12,'bold'),command= minus)
minus.place(x=210,y=160,height=30,width=40)
multiply=Button(frame,text='*',font=('times new roman',12,'bold'),command=multiply)
multiply.place(x=210,y=210,height=30,width=40)
divide=Button(frame,text='/',font=('times new roman',12,'bold'),command= divide)
divide.place(x=210,y=260,height=30,width=40)
equal=Button(frame,text='=',font=('times new roman',12,'bold'),command=equal)
equal.place(x=150,y=260,height=30,width=40)
ac=Button(frame,text='C',font=('times new roman',12,'bold'),command=ac)
ac.place(x=30,y=260,height=30,width=40)

window.mainloop()