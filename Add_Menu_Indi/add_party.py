"""
==== Description ====
This class is used to acquire information to add Parties to the
database.

"""
from __future__ import annotations
from Add_Menu_Indi import Add_Menu
import tkinter
from tkinter import *
from tkinter import messagebox
from Indivijuval import Party
from Database import insert_individual


class AddParty:
    """
    A class that represents the add parties window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.geometry("700x700")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
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
        party_address_label = Label(self.main_frame,
                                       text="Supplier Address: ")
        party_address_label.grid(column=1, row=3)
        party_address_label = Label(self.main_frame,
                                       text="Address Line 2: ")
        party_address_label.grid(column=1, row=4)
        party_address_label = Label(self.main_frame,
                                       text="Address Line 3: ")
        party_address_label.grid(column=1, row=5)

        # Creating party address entry
        party_address_entry1 = Entry(self.main_frame, width=100)
        party_address_entry1.grid(column=2, row=3)

        # Creating party address entry
        party_address_entry2 = Entry(self.main_frame, width=100)
        party_address_entry2.grid(column=2, row=4)

        # Creating party address entry
        party_address_entry3 = Entry(self.main_frame, width=100)
        party_address_entry3.grid(column=2, row=5)

        # Creating create button
        create = Button(self.bottom_frame, text="Create",
                        command=lambda: self.create_button(
                                   party_name_entry.get(),
                                   party_short_entry.get(),
                                   party_address_entry1.get(),
                                   party_address_entry2.get(),
                                   party_address_entry3.get()))
        create.bind("<Return>", lambda event: self.create_button(
                                   party_name_entry.get(),
                                   party_short_entry.get(),
                                   party_address_entry1.get(),
                                   party_address_entry2.get(),
                                   party_address_entry3.get()))

        create.grid(column=0, row=0, ipadx=20)
        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back())
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Add_Menu.execute()

    def create_button(self, name: str, short_name: str, add1: str, add2: str, add3: str):

        if len(name) == 0 or len(short_name) == 0 or len(add1) == 0:
            messagebox.showwarning(title="Error",
                                   message=" Please fill the name, short name"
                                           " and Address Fields!")
        else:
            address = add1 + ", " + add2 + ", " + add3
            party = Party.create_party(name, short_name, address)
            # Add into database
            insert_individual.insert_party(party)
            messagebox.showinfo(title="Complete", message="Party Added!")
            self.back()


def execute():
    new_window = AddParty()
    new_window.show_main_window()
