from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("TO DO LIST")
window.geometry('400x500')

heading=Label(text="TO DO LIST",font=("Rangile",24,'bold'),fg='red')
heading.place(x=115,y=0)


#Frame
frame=Frame(window,height=250,width=300,highlightbackground="green",highlightthickness=2)
frame.place(x=50,y=50)
listbox=Listbox(window)

tasklist = Listbox(frame, font=('times new roman', 12, 'bold'), fg='white', bg='#6F8FAF',selectmode=EXTENDED)
tasklist.place(x=2, y=2, height=243, width=290)

scrollbar = Scrollbar(window, command=tasklist.yview,width=12)
scrollbar.place(x=336, y=54, height=240)
tasklist.config(yscrollcommand=scrollbar.set)


getdata=Entry(window,width=35,highlightbackground='black',highlightthickness=1)
getdata.place(x=50,y=330,height=25)

#Functions

def show_list():
    with open("ani.txt",'r')as f:
        data=f.readlines()
        if len(data)!=0:
            for i in data:
                tasklist.insert(END,i)

show_list()
size=tasklist.size()

def add_data():
    task=getdata.get()
    tasklist.insert(END,task)
    getdata.delete(0,END)

def create():
    global size
    with open("ani.txt",'r')as f:
        data=f.readlines()
    if len(data)==0:
        task_count=tasklist.size()
        for i in range(task_count):
            task = tasklist.get(i)
            with open ("ani.txt",'a')as f:
                f.write(f"{task}\n")
        size=tasklist.size()
        messagebox.showinfo(title='Confirmation', message='You created tasklist successfully  !!')
    else:
        messagebox.showerror(title='ATTENTION',message='You allready created task list')


def update():
    global size
    task_count = tasklist.size()
    for i in range(size,task_count):
        task = tasklist.get(i)
        with open("ani.txt", 'a') as f:
            f.write(f"{task}\n")
    size=tasklist.size()
    messagebox.showinfo(title='UPDATE', message='You update tasklist successfully  !!')

def delete():
    todelete = tasklist.curselection()
    for i in todelete:
        data = tasklist.get(i)
        tasklist.delete(i)
        with open("ani.txt", "r") as file:
            lines = file.readlines()
        filtered_lines = [line for line in lines if line.strip() != data.strip()]
        with open("ani.txt", "w") as file:
            file.writelines(filtered_lines)
        messagebox.showinfo(title='DELETE', message='Your deleted task successfully  !!')

def done():
    change=tasklist.curselection()
    for i in change:
        data=tasklist.get(i)
        with open('ani.txt', 'r', encoding="utf-8") as file:
            file_content = file.read()
        newdata=f"{data} ✔"
        modified_content = file_content.replace(data, newdata)

        with open('ani.txt', 'w', encoding="utf-8") as file:
            file.write(modified_content)
        tasklist.insert(change,newdata)
        tasklist.itemconfig(i, fg='green')
        messagebox.showinfo(title='COMPLITION', message='You completed task successfully  !!')
        tasklist.delete(i+1)



#Button
add=Button(window,text='ADD',bg='green',width=9,command=add_data)
add.place(x=275,y=330,height=25)

create=Button(window,text='CREATE',bg='green',width=15,command=create)
create.place(x=65,y=380,height=30)

update=Button(window,text='UPDATE',bg='green',width=15,command=update)
update.place(x=220,y=380,height=30)

delete=Button(window,text='DELETE',bg='green',width=15,command=delete)
delete.place(x=65,y=430,height=30)

done=Button(window,text='DONE',bg='green',width=15,command=done)
done.place(x=220,y=430,height=30)

window.mainloop()