"""
==== Description ====
This class is used to select the report that needs to be seen,

"""
from __future__ import annotations
from typing import List
from View_Menu import multiple_party_selector
from Database import retrieve_indivijual, efficiency
from Reports import khata_report, supplier_register_report, payment_list_report, payment_list_summary, grand_total_report
from Reports import legacy_payment_list
from Main import MainMenu

import tkinter
from tkinter import *


class ReportSelector:
    """
    A class that represents the report selector window.

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """

    options = ["Khata Report", "Supplier Register", "Payment List", "Payment List Summary", "Grand Total List",
               "Legacy Payment List"]

    def __init__(self, start_date: str, end_date: str, supplier_ids: List[int], party_ids: List[int]) -> None:

        self.window = tkinter.Tk()
        self.window.title("Report Menu")
        self.window.bind("<Escape>", lambda event: self.back())
        # Creating the main frame
        self.main_frame = Frame(self.window)
        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.string_var = StringVar(self.main_frame)
        self.string_var.set(self.options[0])

        self.start_date = start_date
        self.end_date = end_date
        self.supplier_ids = supplier_ids
        self.party_ids = party_ids
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

        select_button.grid(column=3, row=1)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back())
        back_button.pack()

        # Creating back button
        main_button = Button(self.bottom_frame, text="<<Main Menu",
                             command=lambda: self.back_main_button())
        main_button.pack()

        self.main_frame.grid(column=0, row=0)
        self.bottom_frame.grid(column=0, row=1)

    def on_select(self, select: str):

        smart_ids = efficiency.smart_selection(self.supplier_ids, self.party_ids, self.start_date, self.end_date)
        if select == self.options[0]:
            khata_report.execute(smart_ids[0], smart_ids[1], self.start_date, self.end_date)
        elif select == self.options[1]:
            supplier_register_report.execute(smart_ids[0], smart_ids[1], self.start_date, self.end_date)
        elif select == self.options[2]:
            payment_list_report.execute(smart_ids[0], smart_ids[1], self.start_date, self.end_date)
        elif select == self.options[3]:
            payment_list_summary.execute(smart_ids[0], smart_ids[1], self.start_date, self.end_date)
        elif select == self.options[4]:
            grand_total_report.execute(smart_ids[0], smart_ids[1], self.start_date, self.end_date)
        else:
            legacy_payment_list.execute(smart_ids[0], smart_ids[1], self.start_date, self.end_date)

    def back(self):
        self.window.destroy()
        multiple_party_selector.execute(self.start_date, self.end_date, self.supplier_ids)

    def back_main_button(self) -> None:
        """
        Go back to the main menu
        """
        self.window.destroy()
        MainMenu.execute()

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()


def execute(start_date: str, end_date: str, supplier_ids: List[int], party_ids: List[int]):
    new_window = ReportSelector(start_date, end_date, supplier_ids, party_ids)
    new_window.show_main_window()

