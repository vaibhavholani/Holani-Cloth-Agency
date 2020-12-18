"""
==== Description ====
This class is used to acquire information to add register_entrys to the
database.

"""
from __future__ import annotations
from Add_Menu_Indi import Add_Menu
from Indivijuval import Bank
import tkinter
from tkinter import *
from tkinter import messagebox
from Database import insert_individual


class AddBank:
    """
    A class that represents the add register_entrys window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add Bank")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.show_main_window()

    def create_main_frame(self) -> None:
        # Creating bank name label
        bank_name_label = Label(self.main_frame, text="Bank Name: ")
        bank_name_label.grid(column=1, row=1)

        # Creating bank name entry
        bank_name_entry = Entry(self.main_frame, width=100)
        bank_name_entry.grid(column=2, row=1)

        # Creating bank address label
        bank_address_label = Label(self.main_frame, text="Bank Address: ")
        bank_address_label.grid(column=1, row=3)

        # Creating bank address entry
        bank_address_entry = Entry(self.main_frame, width=100)
        bank_address_entry.grid(column=2, row=3)

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create",
                               command=lambda: self.create
                               (bank_name_entry.get(),
                                bank_address_entry.get()))

        create_button.grid(column=0, row=0, ipadx=20)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back())
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Add_Menu.execute()

    def create(self, name: str, address: str):
        if len(name) == 0 or len(address) == 0:
            messagebox.showwarning(title="Error",
                                   message=" Please fill the name, short name"
                                           " and Address Fields!")
        else:
            bank = Bank.create_bank(name, address)
            # Database here
            insert_individual.insert_bank(bank)
            messagebox.showinfo(title="Complete", message="Bank Added!")
            self.back()

def execute():
    new_window = AddBank()
    new_window.show_main_window()
