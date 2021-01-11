"""
==== Description ====
This class is used to select multiple parties for reports.

"""
from __future__ import annotations
from Database import retrieve_indivijual
from View_Menu import multiple_party_selector, date_selector
import bisect
import tkinter
from tkinter import *
from tkinter import messagebox


class Selector:
    """
    A class that represents the choose multiple suppliers Window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    def __init__(self, start_date: str, end_date: str) -> None:
        self.window = tkinter.Tk()
        self.window.title("Choose Suppliers")

        # Creating the main frame
        self.main_frame = Frame(self.window)

        # Creating the main-right frame
        self.main_right_frame = Frame(self.window)

        # Creating a list of Selected Supplier Names
        self.selected_names = []

        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.master = retrieve_indivijual.get_all_supplier_names()

        # Creating an alias of the master copy of supplier names
        self.suppliers = self.master

        self.start_date = start_date
        self.end_date = end_date

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
        category_label = Label(self.main_frame, text="Choose Suppliers ")
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
        back_button.grid(column=2, row=1, columnspan=2, ipadx=20, padx=90, ipady=10, pady=10)

        # Creating Add Button
        add_button = Button(self.bottom_frame, text="Add",
                            command=lambda: self.on_select_add(
                                listbox.get(listbox.curselection())))

        add_button.grid(column=0, row=0, ipadx=20, padx=90, ipady=10,
                        pady=10)

        # Creating Select Button
        select_button = Button(self.bottom_frame, text="Select",
                               command=lambda: self.on_select())

        select_button.grid(column=0, row=1, columnspan=2, ipadx=20, padx=90, ipady=10,
                           pady=10)

        # Creating Select All Button
        select_all_button = Button(self.bottom_frame, text="Select All",
                                   command=lambda: self.add_all())
        select_all_button.grid(column=2, row=0, ipadx=20, padx=90, ipady=10,
                               pady=10)

        # Creating Select All Button
        select_all_button = Button(self.bottom_frame, text="Delete All",
                                   command=lambda: self.del_all())
        select_all_button.grid(column=3, row=0, ipadx=20, padx=90, ipady=10,
                               pady=10)
        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=2)
        self.create_main_right_frame()

    def create_main_right_frame(self):
        """
        Display all the selected names
        """
        # Label
        selected_label = Label(self.main_right_frame, text="Selected Names  ")
        selected_label.grid(column=0, row=1)
        # Listbox scrollbar
        scrollbar2 = Scrollbar(self.main_right_frame)
        scrollbar2.grid(column=2, row=1)

        # Creating Listbox
        listbox2 = Listbox(self.main_right_frame, name="listbox2", selectmode=SINGLE,
                          width=100, yscrollcommand=scrollbar2.set)
        listbox2.insert(END, *self.selected_names)
        listbox2.grid(column=1, row=1)

        # Creating Select Button
        select_button = Button(self.bottom_frame, text="Delete",
                               command=lambda: self.on_select_del(listbox2.get(listbox2.curselection())))

        select_button.grid(column=1, row=0, ipadx=20, padx=90, ipady=10,
                           pady=10)

        # Creating

        self.main_right_frame.grid(column=0, row=1, pady=10)

    def update_list(self, search: str) -> None:

        self.suppliers = \
            [element for element in self.master if search in element]

        listbox = self.main_frame.nametowidget("listbox")
        listbox.delete(0, END)
        listbox.insert(END, *self.suppliers)

    def on_select_add(self, select: str):
        if select not in self.selected_names:
            bisect.insort(self.selected_names, select)
            listbox2 = self.main_right_frame.nametowidget("listbox2")
            listbox2.delete(0, END)
            listbox2.insert(END, *self.selected_names)

    def on_select_del(self, select: str):
        self.selected_names.remove(select)
        listbox2 = self.main_right_frame.nametowidget("listbox2")
        listbox2.delete(0, END)
        listbox2.insert(END, *self.selected_names)

    def add_all(self):
        self.selected_names = self.master.copy()
        listbox2 = self.main_right_frame.nametowidget("listbox2")
        listbox2.delete(0, END)
        listbox2.insert(END, *self.selected_names)

    def del_all(self):
        self.selected_names = []
        listbox2 = self.main_right_frame.nametowidget("listbox2")
        listbox2.delete(0, END)
        listbox2.insert(END, *self.selected_names)

    def on_select(self):
        if len(self.selected_names) == 0:
            messagebox.showwarning(title="No supplier Selected", message="Please select a supplier")
        else:
            self.window.destroy()
            multiple_party_selector.execute(self.start_date, self.end_date, self.selected_names)

    def callback(self, sv: StringVar):
        self.update_list(sv.get())

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def back_button(self) -> None:
        self.window.destroy()
        date_selector.execute()


def execute(sdate: str, edate: str) -> None:
    new_window = Selector(sdate, edate)
    new_window.show_main_window()
