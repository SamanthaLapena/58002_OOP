from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.label_title = Label(window, text = "My Full Name", fg = "red", font = "verdana")
        self.label_title.place(x=200, y=40)

        self.label_firstname = Label(window, text = "Enter Given Name:", fg = "red")
        self.label_firstname.place(x=100, y=80)

        self.label_middlename = Label(window, text = "Enter Middle Name:", fg = "red")
        self.label_middlename.place(x=100, y=110)

        self.label_lastname = Label(window, text = "Enter Last Name:", fg = "red")
        self.label_lastname.place(x=100, y=140)

        self.label_fullname = Label(window, text = "My Full Name is:", fg = "red")
        self.label_fullname.place(x=100, y=180)

        self.txt_firstname = Entry(window, bd=2)
        self.txt_firstname.place(x=275, y=80)

        self.txt_middlename = Entry(window, bd=2)
        self.txt_middlename.place(x=275, y=110)

        self.txt_lastname = Entry(window, bd=2)
        self.txt_lastname.place(x=275, y=140)

        self.txt_fullname = Entry(window, bd=2, width=30)
        self.txt_fullname.place(x=275, y=180)

        self.btn_dsplyflnm = Button(window, text="Show Full Name", command=self.display)
        self.btn_dsplyflnm.place(relx=0.5, y=230, anchor=CENTER)

        self.btn_clearall = Button(window, text="Clear All", command=self.clear_all)
        self.btn_clearall.place(relx=0.5, y=260, anchor=CENTER)

    def display(self):
        self.txt_fullname.delete(0, END)
        firstname = str(self.txt_firstname.get())
        middlename = str(self.txt_middlename.get())
        lastname = str(self.txt_lastname.get())
        fullname = firstname + " " + middlename + " " + lastname + " "
        self.txt_fullname.insert(END, str(fullname))

    def clear_all(self):
        self.txt_firstname.delete(0, END)
        self.txt_middlename.delete(0, END)
        self.txt_lastname.delete(0, END)
        self.txt_fullname.delete(0, END)


window = Tk()
MyWindow(window)
window.geometry("500x300+10+10")
window.mainloop()
