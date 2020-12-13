"""
==== Description ====
This class is used to add Register Entry and Memo Entry to the
database.

"""

from __future__ import annotations
from Add_Menu_Entity import supplier_selector, memo_entry
from Main import MainMenu
from typing import List
import tkinter
from tkinter import *


class AddWindow:
    """
    A class that represents the add Window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    options = ["Register Entry", "Memo Entry"]

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add Entry")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

    def create_main_frame(self) -> None:

        # Creating Category Label
        category_label = Label(self.main_frame, text="Select a Category: ")
        category_label.grid(column=1, row=1)

        # Creating Spinner
        category_spinner = Spinbox(self.main_frame, values=tuple(self.options))
        category_spinner.grid(column=2, row=1)

        # Creating Select Button
        select_button = Button(self.main_frame, text="Select",
                               command=
                               lambda:
                               self.on_select(category_spinner.get()))
        select_button.grid(column=3, row=1)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back())
        back_button.pack()

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def on_select(self, select: str):

        self.window.destroy()
        supplier_selector.execute(select)

    def back(self):
        self.window.destroy()
        MainMenu.execute()

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()


def execute() -> None:
    new_window = AddWindow()
    new_window.show_main_window()






