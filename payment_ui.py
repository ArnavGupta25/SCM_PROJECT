import sqlite3
from tkinter import *
from tkinter import messagebox
import main

class Payment:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("PAYMENT")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="PAYMENT", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # room no label
        self.room_no_label = Label(bottom, font=('arial', 20, 'bold'), text="ENTER THE ROOM NUMBER :", fg="#15d3ba", anchor="center")
        self.room_no_label.grid(row=2, column=2, padx=10, pady=10)

        # text enter field
        self.room_number = IntVar()
        self.room_no_entry = Entry(bottom, width=5, text=self.room_number)
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=10)

        # amount label
        self.amount_label = Label(bottom, font=('arial', 20, 'bold'), text="ENTER THE AMOUNT :", fg="#15d3ba", anchor="center")
        self.amount_label.grid(row=4, column=2, padx=10, pady=10)

        # text enter field
        self.amount_value = IntVar()
        self.amount_entry = Entry(bottom, width=10, text=self.amount_value)
        self.amount_entry.grid(row=4, column=3, padx=10, pady=10)

        # create submit button
        self.submit_button = Button(bottom, text="SUBMIT", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15, fg="black", anchor="center", command=self.submit)
        self.submit_button.grid(row=8, column=2, padx=10, pady=10)

        # create home button
        self.home_button = Button(bottom, text="HOME", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15, fg="black", anchor="center", command=main.home_ui)
        self.home_button.grid(row=8, column=3, padx=10, pady=10)

    def submit(self):
        room_number = self.room_number.get()
        amount = self.amount_value.get()

        conn = sqlite3.connect('Hotel.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Payment (room_number NUMBER, amount NUMBER)')
            cursor.execute('INSERT INTO Payment (room_number, amount) VALUES (?, ?)', (room_number, amount))
            conn.commit()

            self.room_no_entry.delete(0, END)
            self.amount_entry.delete(0, END)

            messagebox.showinfo("Payment Successful", "Thank You, Your Payment is successful!".format(amount, room_number))

def payment_ui():
    root = Tk()
    application = Payment(root)
    root.mainloop()
