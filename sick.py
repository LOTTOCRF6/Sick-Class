from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Sick Class")
root.geometry("600x500")
root.config(bg="Green")


# Parent class of influenza and cancer classes
class Sick:
    def __init__(self):
        # The labels of the sick system
        sickness_code = Label(root, text="Sickness Code:")
        sickness_code.place(x=25, y=150, anchor="w")
        # D.T
        treatment_duration = Label(root, text="Duration of Treatment:")
        treatment_duration.place(x=25, y=200, anchor="w")
        # Duration unit
        duration_unit = Label(root, text="Weeks/Months")
        duration_unit.place(x=390, y=188)
        # D.P.N
        doc_prac_num = Label(root, text="Doctor's Practice Number:")
        doc_prac_num.place(x=25, y=250, anchor="w")

        fee = Label(root, text="Scan/Consultation Fee:")
        fee.place(x=25, y=300, anchor="w")

        amount_paid_label = Label(root, text="Amount paid for treatment:")
        amount_paid_label.place(x=25, y=400)

        # Creating the entry boxes
        self.sick_id = Entry(root)
        self.duration = Entry(root, width=10)
        self.doc_id = Entry(root)
        self.scan_or_consult = Entry(root)

        self.sick_id.place(x=300, y=135)
        self.duration.place(x=300, y=185)
        self.doc_id.place(x=300, y=235)
        self.scan_or_consult.place(x=300, y=285)

        # radiobuttons
        self.v = IntVar()
        cancer_radio = Radiobutton(root, text="Cancer", variable=self.v, value=1, bg="Green")
        influenza_radio = Radiobutton(root, text="Influenza", variable=self.v, value=2, bg="green")

        cancer_radio.place(x=20, y=330)
        influenza_radio.place(x=20, y=360)

        # calculate, clear and exit buttons

        def calculate():  # This function is to redirect the calculation based on the radio button selected
            radio = self.v.get()
            if radio == 1:
                can = Cancer(self.scan_or_consult.get())
            elif radio == 2:
                flu = Influenza(self.scan_or_consult.get())

        calc_btn = Button(root, text="Calculate", command=calculate, bg="Orange", fg="white")
        calc_btn.place(x=25, y=450)

        def clear():  # This function clears entry fields
            self.sick_id.delete(0, 'end')
            self.duration.delete(0, 'end')
            self.doc_id.delete(0, 'end')
            self.scan_or_consult.delete(0, 'end')

        clear_btn = Button(root, text="Clear", command=clear, bg="Blue", fg="white")
        clear_btn.place(x=225, y=450)


# Child of sick class for cancer calculation and display
class Cancer(Sick):

    def __init__(self, scan):
        amount_paid_display = Label(root, text="")
        amount_paid_display.place(x=225, y=400)
        medication = 400
        self.scan = scan

        if float(scan) > 600:
            messagebox.showinfo("", "Sorry we cannot treat you")
        else:
            amount_paid = float(scan) + medication
            amount_paid_display.config(text="R"+str(round(amount_paid, 4)))


# Child of sick class for influenza calculation and display
class Influenza(Sick):

    def __init__(self, consult):
        x = StringVar()
        amount_paid_display = Label(root, textvariable=x)
        amount_paid_display.place(x=225, y=400)
        medication = 350.50
        self.consult = consult
        consult = float(consult)

        if consult > 600:
            consult = 0.98*consult
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")
        else:
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")


exit_btn = Button(root, text="Exit", command=root.destroy, bg="Red", fg="white").place(x=425, y=450)
# tkinter stuff creating window


app = Sick()

root.mainloop()