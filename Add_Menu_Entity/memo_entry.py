"""
==== Description ====
This class is used to acquire information to add memo_entry to the
database.

"""
from __future__ import annotations
from Add_Menu_Entity import new_entry
from typing import List
import tkinter
from tkinter import *


class AddMemoEntry:
    """
    A class that represents the add memo_entry window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add Memo entry")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.show_main_window()

    def create_main_frame(self) -> None:

        memo_entry_short_label = Label(self.main_frame,
                                       text="Party Short Name: ")
        memo_entry_short_label.grid(column=1, row=2)

        # Creating memo_entry name entry
        memo_entry_short_entry = Entry(self.main_frame, width=100)
        memo_entry_short_entry.grid(column=2, row=2)

        # Creating memo_entry address label
        memo_entry_address_label = Label(self.main_frame,
                                             text="Supplier Short Name: ")
        memo_entry_address_label.grid(column=1, row=3)

        # Creating memo_entry address entry
        memo_entry_address_entry = Entry(self.main_frame, width=100)
        memo_entry_address_entry.grid(column=2, row=3)

        # Creating memo_entry address label
        memo_entry_address_label = Label(self.main_frame,
                                             text="Amount: ")
        memo_entry_address_label.grid(column=1, row=4)

        # Creating memo_entry address entry
        memo_entry_address_entry = Entry(self.main_frame, width=100)
        memo_entry_address_entry.grid(column=2, row=4)

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create")
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

    def back_button(self)-> None:
        self.window.destroy()
        new_entry.execute()


def execute() -> None:
    new_window = AddMemoEntry()
    new_window.show_main_window()
