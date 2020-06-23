"""
==== Description ====
This class is used to acquire information to add Suppliers to the
database.

"""
from __future__ import annotations
from typing import List
import tkinter
from tkinter import *


class AddSupplier:
    """
    A class that represents the add suppliers window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add supplier")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.show_main_window()

    def create_main_frame(self) -> None:
        # Creating supplier name label
        supplier_name_label = Label(self.main_frame, text="Supplier name: ")
        supplier_name_label.grid(column=1, row=1)

        # Creating supplier name entry
        supplier_name_entry = Entry(self.main_frame, width=100)
        supplier_name_entry.grid(column=2, row=1)

        supplier_short_label = Label(self.main_frame, text="Short name: ")
        supplier_short_label.grid(column=1, row=2)

        # Creating supplier name entry
        supplier_short_entry = Entry(self.main_frame, width=100)
        supplier_short_entry.grid(column=2, row=2)

        # Creating supplier address label
        supplier_address_label = Label(self.main_frame,
                                       text="Supplier Address: ")
        supplier_address_label.grid(column=1, row=3)

        # Creating supplier address entry
        supplier_address_entry = Entry(self.main_frame, width=100)
        supplier_address_entry.grid(column=2, row=3)

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create")
        create_button.grid(column=0, row=0, ipadx=20)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back")
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()


new_window = AddSupplier()
new_window.show_main_window()
