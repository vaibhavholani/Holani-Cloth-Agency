"""
==== Description ====
This class is used to acquire information to add Parties to the
database.

"""
from __future__ import annotations
from typing import List
import tkinter
from tkinter import *


class AddParty :
    """
    A class that represents the add parties window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add Party")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.show_main_window()

    def create_main_frame(self) -> None:
        # Creating party name label
        party_name_label = Label(self.main_frame, text="Party name: ")
        party_name_label.grid(column=1, row=1)

        # Creating party name entry
        party_name_entry = Entry(self.main_frame, width=100)
        party_name_entry.grid(column=2, row=1)

        party_short_label = Label(self.main_frame, text="Short name: ")
        party_short_label.grid(column=1, row=2)

        # Creating party name entry
        party_short_entry = Entry(self.main_frame, width=100)
        party_short_entry.grid(column=2, row=2)

        # Creating party address label
        party_address_label = Label(self.main_frame, text="Party Address: ")
        party_address_label.grid(column=1, row=3)

        # Creating party address entry
        party_address_entry = Entry(self.main_frame, width=100)
        party_address_entry.grid(column=2, row=3)

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


new_window = AddParty()
new_window.show_main_window()
