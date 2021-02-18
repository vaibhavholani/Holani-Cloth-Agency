"""
==== Description ====
This class is used select date a range of dates

"""
from __future__ import annotations
import tkinter
import datetime
from View_Menu import multiple_supplier_selector
from Add_Menu_Entity import gr_entry
from Main import MainMenu
from tkinter import messagebox
from tkinter import *


class DateSelector:
    """
    A class that represents Date Selector Window
    """

    def __init__(self, option: str = "reports", supplier_name: str = "", party_name: str = ""):
        # The main window
        self.window = tkinter.Tk()
        self.window.title("Date Selector")
        self.window.bind("<Escape>", lambda event: self.back_button())
        # Creating top frame
        self.first_frame = Frame(self.window, highlightbackground="black",
                                 highlightcolor="black",
                                 highlightthickness=1, width=100)
        self.second_frame = Frame(self.window, highlightbackground="black",
                                  highlightcolor="black",
                                  highlightthickness=1, width=100)
        self.bottom_frame = Frame(self.window)
        self.option = option
        self.supplier_name = supplier_name
        self.party_name = party_name

    def create_all_frames(self):
        """
        Add the elements in all frames
        """
        # making text variables
        # Creating StringVar
        sdate = StringVar()
        sdate.trace("w", lambda name, index, mode, sv=sdate: self.callback_md(sv, sdate_month))
        smonth = StringVar()
        smonth.trace("w", lambda name, index, mode, sv=smonth: self.callback_md(sv, sdate_year))
        syear = StringVar()
        syear.trace("w", lambda name, index, mode, sv=syear: self.callback_year(sv, edate_day))

        edate = StringVar()
        edate.trace("w", lambda name, index, mode, sv=edate: self.callback_md(sv, edate_month))
        emonth = StringVar()
        emonth.trace("w", lambda name, index, mode, sv=emonth: self.callback_md(sv, edate_year))

        # making entries
        start_date_label = Label(self.first_frame, text="Starting Date: ")
        start_date_label.pack(side=LEFT)
        sdate_day = Entry(self.first_frame, textvariable=sdate)
        sdate_day.focus()
        sdate_day.pack(side=LEFT)
        s_slash1 = Label(self.first_frame, text="/ ")
        s_slash1.pack(side=LEFT)
        sdate_month = Entry(self.first_frame, textvariable=smonth)
        sdate_month.pack(side=LEFT)
        s_slash2 = Label(self.first_frame, text="/ ")
        s_slash2.pack(side=LEFT)
        sdate_year = Entry(self.first_frame, textvariable=syear)
        sdate_year.pack(side=LEFT)

        self.first_frame.grid(row=1, column=0, pady=10, padx=10)

        # Creating Second Frame
        end_date_label = Label(self.second_frame, text="Ending Date: ")
        end_date_label.pack(side=LEFT)
        edate_day = Entry(self.second_frame,textvariable=edate)
        edate_day.pack(side=LEFT)
        e_slash1 = Label(self.second_frame, text="/ ")
        e_slash1.pack(side=LEFT)
        edate_month = Entry(self.second_frame, textvariable=emonth)
        edate_month.pack(side=LEFT)
        e_slash2 = Label(self.second_frame, text="/ ")
        e_slash2.pack(side=LEFT)
        edate_year = Entry(self.second_frame)
        edate_year.pack(side=LEFT)
        edate_year.bind("<Return>", lambda event: self.select_button(sdate_day.get(),
                                                                        sdate_month.get(),
                                                                        sdate_year.get(),
                                                                        edate_day.get(),
                                                                        edate_month.get(),
                                                                        edate_year.get()))

        self.second_frame.grid(row=2, column=0, pady=10, padx=10)

        # Creating bottom frame

        select_button = Button(self.bottom_frame, text="Select", command=lambda: self.select_button(sdate_day.get(),
                                                                                                    sdate_month.get(),
                                                                                                    sdate_year.get(),
                                                                                                    edate_day.get(),
                                                                                                    edate_month.get(),
                                                                                                    edate_year.get()))
        select_button.bind("<Return>", lambda event: self.select_button(sdate_day.get(),
                                                                       sdate_month.get(),
                                                                       sdate_year.get(),
                                                                       edate_day.get(),
                                                                       edate_month.get(),
                                                                       edate_year.get()))

        back_button = Button(self.bottom_frame, text="Back", command=lambda: self.back_button())
        select_button.grid(row=0, column=0, pady=10, padx=10, ipadx=10, ipady=10)
        back_button.grid(row=0, column=1, pady=10, padx=10, ipadx=10, ipady=10)

        self.bottom_frame.grid(row=3, column=0, pady=10, padx=10)

    def select_button(self, s1: str, s2: str, s3: str, e1: str, e2: str, e3: str):
        """
        Select and verify the dates
        """

        try:
            int(s1)
            int(s2)
            int(s3)
            int(e1)
            int(e2)
            int(e3)
            date1 = s1 + "/" + s2 + "/" + s3
            date2 = e1 + "/" + e2 + "/" + e3
            validate(date1)
            validate(date2)
            self.window.destroy()
            if self.option != "reports":
                gr_entry.execute(self.supplier_name, self.party_name, date1, date2)
            else:
                multiple_supplier_selector.execute(date1, date2)

        except ValueError:
            messagebox.showwarning(title="Value Error", message="Please enter valid dates")

    def create_main_window(self):
        """
        Creates the main_window
        """

        date_label = Label(self.window, text="Please select the starting at ending dates below: ")
        date_label.grid(row=0, column=0)

        self.create_all_frames()

        self.window.mainloop()

    def callback_md(self, sv: StringVar, entry: Entry):
        if len(sv.get()) ==2:
            entry.focus()

    def callback_year(self, sv: StringVar, entry: Entry):
        if len(sv.get()) ==4:
            entry.focus()


    def back_button(self):
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


def execute(option: str = "reports", supplier_name: str = "", party_name: str = ""):
    window = DateSelector(option, supplier_name, party_name)
    window.create_main_window()
