"""
==== Description ====
This class is used to acquire information to add register_entry to the
database.

"""
from __future__ import annotations
from Add_Menu_Entity import party_selector
from Entities import Grentry
from Database import retrieve_gr, retrieve_indivijual
from Main import MainMenu
import tkinter
from tkinter import messagebox
from tkinter import *
import datetime


class AddGREntry:
    """
    A class that represents the add memo_entry window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """
    today = datetime.date.today()
    date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)

    def __init__(self, supplier_name: str, party_name: str, start_date: str, end_date: str) -> None:
        self.window = tkinter.Tk()
        self.window.title("Settle GR entry")
        self.window.geometry("1500x600")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.supplier_name = supplier_name
        self.party_name = party_name
        self.supplier_id = retrieve_indivijual.get_supplier_id_by_name(supplier_name)
        self.party_id = retrieve_indivijual.get_party_id_by_name(party_name)
        self.start_date = start_date
        self.end_date = end_date
        self.gr_amount = retrieve_gr.get_usable_gr(self.supplier_id, self.party_id)

    def create_main_frame(self) -> None:
        # Creating supplier name label
        supplier_name_label = Label(self.main_frame, text="Supplier Name:")
        supplier_name_label.grid(column=1, row=0)

        # Creating name label
        supplier_name_label = Label(self.main_frame, text=self.supplier_name)
        supplier_name_label.grid(column=2, row=0)

        # Creating amount
        gr_entry_amount_label = Label(self.main_frame, text="GR Amount")
        gr_entry_amount_label.grid(column=1, row=1)

        # Creating register_entry name entry
        gr_entry_amount_entry = Label(self.main_frame, text=self.gr_amount)
        gr_entry_amount_entry.grid(column=2, row=1)

        register_entry_short_label = Label(self.main_frame,
                                           text="Party Name: ")
        register_entry_short_label.grid(column=1, row=2)

        # Creating register_entry name entry
        register_entry_short_entry_text = Label(self.main_frame,
                                                text=self.party_name)
        register_entry_short_entry_text.grid(column=2, row=2)

        # Creating amount label
        amount_label = Label(self.main_frame,
                                             text="Amount: ")
        amount_label.grid(column=1, row=4)

        # Creating register_entry amount entry
        amount_entry = Entry(self.main_frame, width=100)
        amount_entry.focus()
        amount_entry.grid(column=2, row=4)

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create",
                               command=lambda: self.create_button(
                                   amount_entry.get()))

        create_button.bind("<Return>", lambda event: self.create_button(amount_entry.get()))

        create_button.grid(column=0, row=0, ipadx=20)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back_button())
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        # Creating back button
        main_button = Button(self.bottom_frame, text="<<Main Menu",
                             command=lambda: self.back_main_button())
        main_button.grid(column=3, row=0, padx=90, ipadx=20)

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def create_button(self, amount: int) -> None:

        try:
            int_amount = int(amount)
            # validate(date)
            Grentry.call(int_amount, self.supplier_name, self.party_name, self.start_date, self.end_date)
            messagebox.showinfo(title="Complete", message="GR Entry Added!")
            self.window.destroy()
            execute(self.supplier_name, self.party_name, self.start_date, self.end_date)
        except ValueError:
            messagebox.showwarning(title="Error",
                                   message="Invalid Amount")

    def back_button(self) -> None:
        self.window.destroy()
        party_selector.execute(self.supplier_name, "Memo Entry")

    def back_main_button(self) -> None:
        """
        Go back to the main menu
        """
        self.window.destroy()
        MainMenu.execute()


def validate(date_text: str):
    """
    Used to validate date format
    """
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD/MM/YYYY")


def execute(supplier_name: str, party_name: str, start_date: str, end_date: str) -> None:
    new_window = AddGREntry(supplier_name, party_name, start_date, end_date)
    new_window.show_main_window()


