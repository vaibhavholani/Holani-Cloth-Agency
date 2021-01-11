"""
==== Description ====
This class is used to select a supplier's register.

"""
from __future__ import annotations
from Add_Menu_Entity import register_entry, new_entry, party_selector
from Database import Lists, retrieve_indivijual
from typing import List
import tkinter
from tkinter import *


class Selector:
    """
    A class that represents the choose supplier Window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self, option: str) -> None:
        self.window = tkinter.Tk()
        self.window.title("Choose Supplier")
        self.window.geometry("1500x1500")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.master = retrieve_indivijual.get_all_supplier_names()

        # Creating an alias of the master copy of supplier names
        self.suppliers = self.master

        # Setting option
        self.option = option

    def create_main_frame(self) -> None:

        # Creating Search Label
        search_label = Label(self.main_frame, text="Search: ")
        search_label.grid(column=1, row=1)

        # Creating StringVar
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback(sv))

        # Creating Search Entry
        search_entry = Entry(self.main_frame, textvariable=sv, width=100)
        search_entry.focus()
        search_entry.grid(column=2, row=1)

        # Creating Choose Label
        category_label = Label(self.main_frame, text="Choose a Supplier ")
        category_label.grid(column=1, row=2)

        # Listbox scrollbar
        scrollbar = Scrollbar(self.main_frame)
        scrollbar.grid(column=3, row=2)

        # Creating Listbox
        listbox = Listbox(self.main_frame, name="listbox", selectmode=SINGLE,
                          width=100, yscrollcommand=scrollbar.set)
        listbox.insert(END, *self.master)
        listbox.grid(column=2, row=2)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back_button())
        back_button.grid(column=1, row=0, ipadx=20, padx=90, ipady=10, pady=10)

        # Creating Select Button
        select_button = Button(self.bottom_frame, text="Select",
                               command=lambda: self.on_select(
                                   listbox.get(listbox.curselection())))

        select_button.bind("<Return>", func=lambda event: self.on_select(
                                   listbox.get(listbox.curselection())))
        select_button.grid(column=0, row=0, ipadx=20, padx=90, ipady=10,
                           pady=10)

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def update_list(self, search: str) -> None:

        self.suppliers = \
            [element for element in self.master if search in element]

        listbox = self.main_frame.nametowidget("listbox")
        listbox.delete(0, END)
        listbox.insert(END, *self.suppliers)

    def on_select(self, select: str):
        self.window.destroy()
        if self.option == "Register Entry":
            register_entry.execute(select)
        else:
            party_selector.execute(select, self.option)

    def callback(self, sv: StringVar):
        self.update_list(sv.get())

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def back_button(self) -> None:
        self.window.destroy()
        new_entry.execute()


def execute(option: str) -> None:
    new_window = Selector(option)
    new_window.show_main_window()


