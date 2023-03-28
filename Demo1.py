from tkinter import *
window = Tk()

window.geometry("500x400+10+10")
window.title("My first GUI")

txt = Entry(window,border = 10)
txt.place(x= 150, y =150)
btn1 = Button(window,text = "Click me this is virus", fg = "blue", bg = "green")
btn1.place(x = 200, y = 200)


lbl = Label(window,text= "My first Demo", font = "Verdana")
lbl.place(x = 150, y = 50)

window.mainloop()