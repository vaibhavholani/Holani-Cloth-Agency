"""
==== Description ====
This class is used to acquire information to add register_entry to the
database.

"""
from __future__ import annotations
from Add_Menu_Entity import supplier_selector
from Entities import RegisterEntry
from Database import retrieve_indivijual, retrieve_register_entry
from Main import MainMenu
import tkinter
from tkinter import messagebox
from tkinter import *
import datetime


class AddRegisterEntry:
    """
    A class that represents the add register_entry window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """
    today = datetime.date.today()

    def __init__(self, supplier_name: str) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add Register Entry")
        self.window.geometry("1500x600")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.supplier_name = supplier_name
        self.supplier_id = retrieve_indivijual.get_supplier_id_by_name(self.supplier_name)
        self.party_names = retrieve_indivijual.get_all_party_names()
        self.selected_parties = []

    def create_main_frame(self) -> None:

        # Creating supplier name label
        supplier_name_label = Label(self.main_frame, text="Supplier Name:")
        supplier_name_label.grid(column=1, row=0)

        # Creating name label
        supplier_name_label = Label(self.main_frame, text=self.supplier_name)
        supplier_name_label.grid(column=2, row=0, columnspan=5)

        # Creating register_entry name label
        bill_number = Label(self.main_frame, text="Bill Number:")
        bill_number.grid(column=1, row=1)
        bill_number.focus()

        # Creating register_entry name entry
        bill_number_entry = Entry(self.main_frame, width=100)
        bill_number_entry.grid(column=2, row=1, columnspan=5)

        # Creating date label
        date_label = Label(self.main_frame, text="Date: ")
        date_label.grid(column=1, row=2)

        # Creating date entry
        date_entry1 = Entry(self.main_frame, width=10)
        date_entry1.insert(0, str(self.today.day))
        Label(self.main_frame, text=" / ").grid(column=3, row=2)
        Label(self.main_frame, text=" / ").grid(column=5, row=2)
        date_entry1.grid(column=2, row=2)
        date_entry2 = Entry(self.main_frame, width=10)
        date_entry2.insert(0, str(self.today.month))
        date_entry2.grid(column=4, row=2)
        date_entry3 = Entry(self.main_frame, width=20)
        date_entry3.insert(0, str(self.today.year))
        date_entry3.grid(column=6, row=2)

        search_label = Label(self.main_frame,
                                           text="Party Name: ")
        search_label.grid(column=1, row=3)

        # Creating register_entry name entry
        # Creating StringVar
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback(sv))

        register_entry_search = Entry(self.main_frame, textvariable=sv, width=100)
        register_entry_search.grid(column=2, row=3, columnspan=5)

        # Creating Listbox
        # Listbox scrollbar
        scrollbar = Scrollbar(self.main_frame)
        listbox = Listbox(self.main_frame, name="listbox", selectmode=SINGLE,
                          width=100, yscrollcommand=scrollbar.set)
        listbox.insert(END, *self.party_names)
        listbox.grid(column=2, row=4, columnspan=5)

        # Creating register_entry amount label
        amount_label = Label(self.main_frame,
                                             text="Amount: ")
        amount_label.grid(column=1, row=5)

        # Creating register_entry amount entry
        amount_entry = Entry(self.main_frame, width=100)
        amount_entry.grid(column=2, row=5, columnspan=5)

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create",
                               command=lambda: self.create_button(
                                   bill_number_entry.get(),
                                   amount_entry.get(),
                                   "{}/{}/{}".format(date_entry1.get(), date_entry2.get(), date_entry3.get()),
                               listbox.get(listbox.curselection())))
        create_button.bind("<Return>", lambda event: self.create_button(
                                   bill_number_entry.get(),
                                   amount_entry.get(),
                                   "{}/{}/{}".format(date_entry1.get(), date_entry2.get(), date_entry3.get()),
        listbox.get(listbox.curselection())))

        create_button.grid(column=0, row=0, ipadx=20)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back_button())
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        # Creating back button
        main_button = Button(self.bottom_frame, text="<<Main Menu",
                             command=lambda: self.back_main_button())
        main_button.grid(column=3, row=0, padx=90, ipadx=20)

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def create_button(self, bill: str, amount: str, date: str, party_name: str) -> None:

        try:
            int_bill = int(bill)
            int_amount = int(amount)
            validate(date)
            party_id = retrieve_indivijual.get_party_id_by_name(party_name)
            if not retrieve_register_entry.check_unique_bill_number(self.supplier_id, party_id, int_bill, date):
                messagebox.showwarning(title="Error",
                                       message="Duplicate Bill Number on the same date")
            else:
                RegisterEntry.call(int_bill, int_amount, self.supplier_name, party_name, date)
                messagebox.showinfo(title="Complete", message="Register Entry Added!")
                self.window.destroy()
                execute(self.supplier_name)
        except ValueError:
            messagebox.showwarning(title="Error",
                                   message="Invalid Amount or "
                                           "Bill Number Entered")

    def update_list(self, search: str) -> None:

        self.selected_parties = \
            [element for element in self.party_names if search in element]

        listbox = self.main_frame.nametowidget("listbox")
        listbox.delete(0, END)
        listbox.insert(END, *self.selected_parties)

    def callback(self, sv: StringVar):
        self.update_list(sv.get())

    def back_button(self) -> None:
        self.window.destroy()
        supplier_selector.execute("Register Entry")

    def back_main_button(self) -> None:
        """
        Go back to the main menu
        """
        self.window.destroy()
        MainMenu.execute()


def validate(date_text: str):
    """
    Used to validate date format
    """
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD/MM/YYYY")


def execute(supplier_name: str) -> None:
    new_window = AddRegisterEntry(supplier_name)
    new_window.show_main_window()


