from tkinter import *
from webbrowser import get


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="My Full Name")
        self.lbl1.place(x=200, y=25)
        self.lbl2 = Label(win, text="Enter Given Name: ")
        self.lbl2.place(x=100, y=65)
        self.lbl3 = Label(win, text="Enter Middle Name: ")
        self.lbl3.place(x=100, y=95)
        self.lbl4 = Label(win, text="Enter last Name: ")
        self.lbl4.place(x=100, y=125)
        self.lbl5 = Label(win, text="My full Name is: ")
        self.lbl5.place(x=100, y=175)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=300, y=65)
        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=300, y=95)
        self.txt4 = Entry(win, bd=1)
        self.txt4.place(x=300, y=125)
        self.txt5 = Entry(win, bd=1)
        self.txt5.place(x=300, y=175)
        self.SFN = Button(win, text="Show Full Name", command=self.add_inputs)
        self.SFN.place(x=200, y=200)

    def add_inputs(self):
        given_name = self.txt2.get()
        middle_name = self.txt3.get()
        last_name = self.txt4.get()
        full_name = f"{given_name} {middle_name} {last_name}"
        self.txt5.delete(0, END)
        self.txt5.insert(END, full_name)

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()
