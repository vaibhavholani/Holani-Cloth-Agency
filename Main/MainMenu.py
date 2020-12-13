import tkinter
from tkinter import *
from Add_Menu_Entity import new_entry
from Add_Menu_Indi import Add_Menu


class MainMenu:
    """
    The first frame of the program.
    Navigate to Add Register Entry, Memo Entry
    Navigate to Add Party, Supplier, Transporter Bank
    """

    def __init__(self):
        self.window = tkinter.Tk()
        self.main_frame = Frame(self.window)

    def create_main_frame(self):

        add_entry_button = Button(self.main_frame, text="Register/Memo Entry",
                                  command=lambda: self.entry_button(),
                                  padx=10, pady=10)
        add_entity_button = Button(self.main_frame, text="Add Menu",
                                   command=lambda: self.entity_button(),
                                   padx=10, pady=10)
        edit_button = Button(self.main_frame, text="Edit Records",
                             padx=10, pady=10)

        add_entry_button.grid(row=0, column=0, pady=10, padx=10)
        add_entity_button.grid(row=1, column=0, pady=10, padx=10)
        edit_button.grid(row=2, column=0, pady=10, padx=10)

        self.main_frame.grid(row=0, column=0)
        self.window.mainloop()

    def entry_button(self):
        self.window.destroy()
        new_entry.execute()

    def entity_button(self):
        self.window.destroy()
        Add_Menu.execute()


def execute():
    window = MainMenu()
    window.create_main_frame()



