"""
==== Description ====
This class is used to add Suppliers, Parties, Transporters and register_entrys to the
database.

"""
from __future__ import annotations
from Main import MainMenu
from Add_Menu_Indi import add_bank, add_party, add_supplier, add_transporter
import tkinter
from tkinter import *


class AddWindow:
    """
    A class that represents the add Window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    options = ["Supplier", "Party", "Transporter", "Bank"]

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.geometry("700x500")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.title("Add Menu")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.string_var = StringVar(self.main_frame)
        self.string_var.set(self.options[0])
        self.show_main_window()

    def create_main_frame(self) -> None:

        # Creating Category Label
        category_label = Label(self.main_frame, text="Select a Category: ")
        category_label.grid(column=1, row=1)

        # Creating Spinner
        category_spinner = OptionMenu(self.main_frame, self.string_var,  *self.options)
        category_spinner.grid(column=2, row=1)

        # Creating Select Button
        select_button = Button(self.main_frame, text="Select",
                               command=lambda: self.on_select
                               (self.string_var.get()))
        select_button.bind("<Return>", lambda event: self.on_select(self.string_var.get()))

        select_button.grid(column=3, row=1)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back())
        back_button.pack()

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def on_select(self, select: str):
        self.window.destroy()
        if select == self.options[0]:
            add_supplier.execute()
        elif select == self.options[1]:
            add_party.execute()
        elif select == self.options[2]:
            add_transporter.execute()
        else:
            add_bank.execute()

    def back(self):
        self.window.destroy()
        MainMenu.execute()

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()


def execute():
    new_window = AddWindow()
    new_window.show_main_window()

