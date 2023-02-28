import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import main

class RoomService:
    def __init__(self, root):
        self.root = root
        # Create a menubar
        self.menu_bar = Menu(root)
        # Add a Room Service menu
        self.room_service_menu = Menu(self.menu_bar, tearoff=0)
        self.room_service_menu.add_command(label="Menu item 1")
        self.room_service_menu.add_command(label="Menu item 2")
        self.menu_bar.add_cascade(label="Room Service", menu=self.room_service_menu)
        # Set the menubar
        self.root.config(menu=self.menu_bar)

        self.root = root
        pad = 3
        self.root.title("ROOM SERVICE")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="ROOM SERVICE", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # room no label
        self.room_no_label = Label(bottom, font=('arial', 20, 'bold'), text="ENTER THE ROOM NUMBER :", fg="#15d3ba", anchor="center")
        self.room_no_label.grid(row=2, column=2, padx=10, pady=10)

        # text enter field
        self.room_number = IntVar()
        self.room_no_entry = Entry(bottom, width=5, text=self.room_number)
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=10)

        # service label
        self.service_label = Label(bottom, font=('arial', 20, 'bold'), text="ENTER THE SERVICE(if required) :", fg="#15d3ba", anchor="center")
        self.service_label.grid(row=4, column=2, padx=10, pady=10)

        # text enter field
        self.service_value = StringVar()
        self.service_entry = Entry(bottom, width=10, text=self.service_value)
        self.service_entry.grid(row=4, column=3, padx=10, pady=10)

        # menu label
        self.menu_label = Label(bottom, font=('arial', 20, 'bold'), text="MENU :", fg="#15d3ba", anchor="center")
        self.menu_label.grid(row=6, column=2, padx=10, pady=10)
        # submit button
        self.submit_button = Button(bottom, text="Submit", command=self.submit)
        self.submit_button.grid(row=8, column=3, padx=10, pady=10)


        # menu options
        self.menu_options = ["Pizza", "Burger", "Fries", "Salad", "Sandwich"]
        self.menu_listbox = Listbox(bottom, selectmode=MULTIPLE)
        for option in self.menu_options:
            self.menu_listbox.insert(END, option)
            self.menu_listbox.grid(row=6, column=3, padx=10, pady=10)

        # menu label
    def update_menu_label(self, selected_item):
        # Update the menu label with the selected item
        self.menu_label.config(text="SELECTED MENU: " + selected_item)
    def submit(self):
        room_number = self.room_number.get()
        service = self.service_value.get()
        menu_selections = self.menu_listbox.curselection()

        if not room_number:
            messagebox.showinfo("Success", "Your request has been submitted.")
            return

        if not service:
            messagebox.showinfo("Success", "Your request has been submitted.")
            return

        if not menu_selections:
            messagebox.showinfo("Success", "Your request has been submitted.")
            return

        menu_items = [self.menu_options[i] for i in menu_selections]
        menu = ", ".join(menu_items)

        # save the data to a database
        conn = sqlite3.connect("hotel.db")
        c = conn.cursor()
        c.execute("INSERT INTO room_service (room_number, service, menu) VALUES (?, ?, ?)", (room_number, service, menu))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Your request has been submitted.")

        
def room_service_ui():
    root = Tk()
    application = RoomService(root)
    root.mainloop()   
