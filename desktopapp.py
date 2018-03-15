from tkinter import *
import backend

window=Tk()

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb1.curselection()[0]
        selected_tuple=lb1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    backend.delete(selected_tuple[0])
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())




def view_command():
    lb1.delete(0,END)
    for row in backend.view():
        lb1.insert(END,row)

def search_command():
    lb1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lb1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lb1.delete(0,END)
    lb1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

lb1=Listbox(window,height=10,width=40)
lb1.grid(row=2,column=0,rowspan=8,columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2,column=2,rowspan=8)

lb1.configure(yscrollcommand=sb.set)
sb.configure(command=lb1.yview)

lb1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",command=window.destroy)
b6.grid(row=7,column=3)







window.mainloop()
