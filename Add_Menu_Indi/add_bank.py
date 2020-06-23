"""
==== Description ====
This class is used to acquire information to add register_entrys to the
database.

"""
from __future__ import annotations
from typing import List
import tkinter
from tkinter import *


class Addregister_entry:
    """
    A class that represents the add register_entrys window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add register_entry")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.show_main_window()

    def create_main_frame(self) -> None:
        # Creating register_entry name label
        register_entry_name_label = Label(self.main_frame, text="register_entry name: ")
        register_entry_name_label.grid(column=1, row=1)

        # Creating register_entry name entry
        register_entry_name_entry = Entry(self.main_frame, width=100)
        register_entry_name_entry.grid(column=2, row=1)

        register_entry_short_label = Label(self.main_frame, text="Short name: ")
        register_entry_short_label.grid(column=1, row=2)

        # Creating register_entry name entry
        register_entry_short_entry = Entry(self.main_frame, width=100)
        register_entry_short_entry.grid(column=2, row=2)

        # Creating register_entry address label
        register_entry_address_label = Label(self.main_frame, text="register_entry Address: ")
        register_entry_address_label.grid(column=1, row=3)

        # Creating register_entry address entry
        register_entry_address_entry = Entry(self.main_frame, width=100)
        register_entry_address_entry.grid(column=2, row=3)

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


new_window = Addregister_entry()
new_window.show_main_window()
