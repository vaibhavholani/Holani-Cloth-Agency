"""
==== Description ====
This class is used to acquire information to add register_entry to the
database.

"""
from __future__ import annotations
from Add_Menu_Entity import supplier_selector
from Entities import RegisterEntry
from typing import List
import tkinter
from tkinter import messagebox
from tkinter import *
import datetime


class AddRegisterEntry:
    """
    A class that represents the add register_entry window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """
    today = datetime.date.today()
    date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)

    def __init__(self, supplier_name: str, party_name: str) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add register_entry")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.supplier_name = supplier_name
        self.party_name = party_name

    def create_main_frame(self) -> None:

        # Creating supplier name label
        supplier_name_label = Label(self.main_frame, text="Supplier Name:")
        supplier_name_label.grid(column=1, row=0)

        # Creating name label
        supplier_name_label = Label(self.main_frame, text=self.supplier_name)
        supplier_name_label.grid(column=2, row=0)

        # Creating register_entry name label
        register_entry_name_label = Label(self.main_frame, text="Bill Number:")
        register_entry_name_label.grid(column=1, row=1)

        # Creating register_entry name entry
        register_entry_name_entry = Entry(self.main_frame, width=100)
        register_entry_name_entry.grid(column=2, row=1)

        register_entry_short_label = Label(self.main_frame,
                                           text="Party Short Name: ")
        register_entry_short_label.grid(column=1, row=2)

        # Creating register_entry name entry
        register_entry_short_entry_text = Label(self.main_frame,
                                                text=self.party_name)
        register_entry_short_entry_text.grid(column=2, row=2)

        # Creating register_entry amount label
        register_entry_address_label = Label(self.main_frame,
                                             text="Amount: ")
        register_entry_address_label.grid(column=1, row=4)

        # Creating register_entry amount entry
        register_entry_address_entry = Entry(self.main_frame, width=100)
        register_entry_address_entry.grid(column=2, row=4)

        # Creating date label
        date_label = Label(self.main_frame, text="Date: ")
        date_label.grid(column=1, row=5)

        # Creating date entry
        date_entry = Entry(self.main_frame, width=100)
        date_entry.insert(0, self.date)
        date_entry.grid(column=2, row=5)

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create",
                               command=lambda: self.create_button(
                                   register_entry_name_entry.get(),
                                   register_entry_address_entry.get(),
                                   date_entry.get()))
        create_button.grid(column=0, row=0, ipadx=20)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back_button())
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def create_button(self, bill: str, amount: str, date: str) -> None:

        try:
            int_bill = int(bill)
            int_amount = int(amount)
            register = RegisterEntry.call(int_bill, int_amount,
                                          self.supplier_name, self.party_name,
                                          date)
            print(register.supplier_name)
        except ValueError:
            messagebox.showwarning(title="Error",
                                   message="Invalid Amount or "
                                           "Bill Number Entered")
            print("Invalid Amount Entered")

    def back_button(self) -> None:
        self.window.destroy()
        supplier_selector.execute("Register Entry")


def execute(supplier_name: str, party_name: str) -> None:
    new_window = AddRegisterEntry(supplier_name, party_name)
    new_window.show_main_window()


