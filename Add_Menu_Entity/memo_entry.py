"""
==== Description ====
This class is used to acquire information to add memo_entry to the
database.

"""
from __future__ import annotations
from Add_Menu_Entity import supplier_selector
from Entities import MemoEntry
import datetime
import tkinter
from tkinter import messagebox
from tkinter import *


class AddMemoEntry:
    """
    A class that represents the add memo_entry window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """
    today = datetime.date.today()
    date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)

    def __init__(self, supplier: str, party: str) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add Memo entry")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        # Setting Supplier and Party
        self.supplier_name = supplier
        self.party_name = party

    def create_main_frame(self) -> None:

        # Creating supplier name label
        supplier_name_label1 = Label(self.main_frame, text="Supplier Name:")
        supplier_name_label1.grid(column=1, row=0)

        # Creating name label
        supplier_name_label2 = Label(self.main_frame, text=self.supplier_name)
        supplier_name_label2.grid(column=2, row=0)

        # Creating party name label
        party_name_label1 = Label(self.main_frame, text="Party Name: ")

        party_name_label1.grid(column=1, row=2)

        # Creating name Label
        party_name_label2 = Label(self.main_frame,
                                  text=self.party_name)

        party_name_label2.grid(column=2, row=2)


        # Creating memo_entry amount label
        memo_entry_address_label = Label(self.main_frame,
                                             text="Amount: ")
        memo_entry_address_label.grid(column=1, row=4)

        # Creating memo_entry amount entry
        memo_entry_address_entry = Entry(self.main_frame, width=100)
        memo_entry_address_entry.grid(column=2, row=4)

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
                                   memo_entry_address_entry.get(),
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

    def create_button(self, amount: str, date: str) -> None:

        try:
            int_amount = int(amount)
            memo = MemoEntry.call(self.supplier_name, self.party_name,
                                  int_amount)
            print(memo.supplier_name)
        except ValueError:
            messagebox.showwarning(title="Error",
                                   message="Invalid Amount Entered")
            print("Invalid Amount Entered")

    def back_button(self)-> None:
        self.window.destroy()
        supplier_selector.execute("Memo Entry")


def execute(supplier: str, party: str) -> None:
    new_window = AddMemoEntry(supplier, party)
    new_window.show_main_window()
