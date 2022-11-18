from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=lst.curselection()[0]
        selected_tuple=lst.get(index)
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
    
def view_command():
    lst.delete(0,END)
    for row in backend.view():
        lst.insert(END,row)

def search_command():
    lst.delete(0,END)
    for row in backend.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        lst.insert(END,row)

def add_command():
    backend.insert(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    lst.delete(0,END)
    lst.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())

window = Tk()

window.wm_title("TV_Series_Watch")

# Label set
l1 = Label(window, text = "Name")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "Main Actors")
l4.grid(row = 1, column = 2)

# Entry set
e1_value = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row = 0, column = 1)

e2_value = StringVar()
e2 = Entry(window, textvariable= e2_value)
e2.grid(row = 0, column = 3)

e3_value = StringVar()
e3 = Entry(window, textvariable= e3_value)
e3.grid(row = 1, column = 1)

e4_value = StringVar()
e4 = Entry(window, textvariable= e4_value)
e4.grid(row = 1, column = 3)

#List displaying
lst = Listbox(window, height = 15, width = 70)
lst.grid(row = 2, column = 0, rowspan = 10, columnspan = 2)

# Scrollbar
sb = Scrollbar(window)
sb.grid(row = 2, column = 2,rowspan = 10)

sbh = Scrollbar(window,orient='horizontal')
sbh.grid(row =10 , column = 2,columnspan= 10)

#List configure
lst.configure(yscrollcommand=sb.set)
sb.configure(command=lst.yview)

lst.bind('<<ListboxSelect>>', get_selected_row)

# Button set
b1 = Button(window, text = "View all", width = 15,command=view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 15, command=search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 15, command=add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 15,command=update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 15,command=delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 15,command=window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()


