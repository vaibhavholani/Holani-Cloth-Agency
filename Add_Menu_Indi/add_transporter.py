"""
==== Description ====
This class is used to acquire information to add transporters to the
database.

"""
from __future__ import annotations
from Add_Menu_Indi import Add_Menu
import tkinter
from tkinter import *
from tkinter import messagebox
from Indivijuval import Transporter
from Database import insert_individual


class AddTransporter:
    """
    A class that represents the add transporters window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.geometry("700x700")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.title("Add Transporter")
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.show_main_window()

    def create_main_frame(self) -> None:
        # Creating transporter name label
        transporter_name_label = Label(self.main_frame,
                                       text="Transporter name: ")
        transporter_name_label.grid(column=1, row=1)

        # Creating transporter name entry
        transporter_name_entry = Entry(self.main_frame, width=100)
        transporter_name_entry.focus()
        transporter_name_entry.grid(column=2, row=1)

        # Creating transporter address label
        transporter_address_label = Label(self.main_frame,
                                          text="Transporter Address: ")
        transporter_address_label.grid(column=1, row=3)

        # Creating transporter address entry
        transporter_address_entry = Entry(self.main_frame, width=100)
        transporter_address_entry.grid(column=2, row=3)

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create",
                               command=lambda:
                               self.create(transporter_name_entry.get(),
                                      transporter_address_entry.get()))

        create_button.grid(column=0, row=0, ipadx=20)

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

    def create(self, name: str, address: str):
        if len(name) == 0 or len(address) == 0:
            messagebox.showwarning(title="Error",
                                   message=" Please fill the name, short name"
                                           " and Address Fields!")
        else:
            transport = Transporter.create_transporter(name, address)
            # Database here
            insert_individual.insert_transporter(transport)
            messagebox.showinfo(title="Complete", message="Transporter Added!")
            self.back()


def execute():
    new_window = AddTransporter()
    new_window.show_main_window()
