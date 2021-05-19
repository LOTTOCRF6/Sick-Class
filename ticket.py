from tkinter import *


root = Tk()
root.title("Ticket Sales")
root.geometry("500x500")
root.config(bg="Green")


class Circle:
    myresult= StringVar()
    variable = StringVar()
    variable.set("Select")
    w = OptionMenu(root, variable, "Soccer", "Movie", "Theatre")
    w.pack()
    w.place(x=190, y=35)

    def __init__(self, master):
        self.lab1 = Label(master, text="Enter CellNumber: ")
        self.lab1.place(x=5, y=5)
        self.myentry = Entry(master)
        self.myentry.place(x=150, y=5)
        self.lab2 = Label(master, text="Select Ticket Category: ")
        self.lab2.place(x=5, y=35)
        self.lab3 = Label(master, text="Number of Ticket Bought: ")
        self.lab3.place(x=5, y=85)
        self.myentry = Entry(master)
        self.myentry.place(x=150, y=5)


x = Circle(root)
root.mainloop()