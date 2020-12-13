"""
==== Description ====
This class is used to acquire information to add memo_entry to the
database.

"""
from __future__ import annotations
from Add_Menu_Entity import party_selector
from Entities import MemoEntry, RegisterEntry
from Database import Lists
import datetime
import tkinter
from tkinter import messagebox
from tkinter import *


class AddMemoEntry:
    """
    A class that represents the add memo_entry window

    ===Attributes===

    window: container for all objects
    options: list containing all the options

    """
    today = datetime.date.today()
    date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)
    radio_options = {"Full": "1", "Partial": "2", "Goods Return": "3"}
    partial_options = {"In-Bill": "1", "No-bill": "2"}

    def __init__(self, supplier: str, party: str) -> None:
        self.window = tkinter.Tk()
        self.window.title("Add Memo entry")

        # Creating top frame
        self.top_frame = Frame(self.window, highlightbackground="black",
                               highlightcolor="black",
                               highlightthickness=1, width=100)

        # Creating the main frame
        self.main_frame = Frame(self.window)

        # Creating the main-left frame
        self.left_frame = Frame(self.main_frame)

        # Creating the main-right frame
        self.right_frame = Frame(self.main_frame, highlightbackground="black",
                                 highlightcolor="black", highlightthickness=1)

        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        # Creating an extra frame for radio buttons (selection mode)
        self.radio_frame = Frame(self.main_frame, highlightbackground="red",
                                 highlightcolor="red", highlightthickness=1)

        # Creating an extra frame for radio buttons (partial mode)
        self.partial_frame = Frame(self.main_frame, highlightbackground="black",
                                 highlightcolor="black", highlightthickness=1)

        # Creating a frame to use partial amount

        self.use_partial_frame = Frame(self.main_frame, highlightbackground="blue",
                                   highlightcolor="blue", highlightthickness=1)


        # Setting Supplier, Party and Total Amount
        self.total = 0
        self.supplier_name = supplier
        self.party_name = party

        # Setting Dynamic Entry
        self.memo_entry_amount_entry = Entry(self.left_frame, width=50)
        self.memo_entry_amount_entry.insert(0, str(self.total))

        # Creating pending bill list
        self.pending_bill = Lists.retrieve_data(self.supplier_name,
                                                self.party_name)

        # Creating Selected bills list
        self.selected_bills = []

        # Selected Mode Tracker
        self.selected_mode = 1

        # Partial Mode Tracker
        self.selected_partial = 1

        # Partial Amount
        self.partial_amount = Lists.retrieve_partial_data(self.supplier_name,
                                                          self.party_name)[0]
        # Use Partial?
        self.use_partial = 0

    def create_main_frame(self) -> None:

        # '''TOP FRAME '''
        # Creating supplier name label
        supplier_name_label1 = Label(self.top_frame, text="Supplier Name:")
        supplier_name_label1.grid(column=1, row=0)

        # Creating name label
        supplier_name_label2 = Label(self.top_frame, text=self.supplier_name)
        supplier_name_label2.grid(column=2, row=0)

        # Creating party name label
        party_name_label1 = Label(self.top_frame, text="Party Name: ")

        party_name_label1.grid(column=1, row=2)

        # Creating name Label
        party_name_label2 = Label(self.top_frame,
                                  text=self.party_name)

        party_name_label2.grid(column=2, row=2)

        # '''MAIN FRAME '''

        Label(self.radio_frame, text="Option: ").pack(side=LEFT)

        # Creating Payment Option Radio Button
        self.radio_button_maker()

        # Creating memo_number label
        memo_number_label = Label(self.left_frame, text="Memo Number: ")
        memo_number_label.grid(column=1, row=3)

        # Creating memo_number entry
        memo_number_entry = Entry(self.left_frame, width=50)
        memo_number_entry.grid(column=2, row=3)

        # Creating memo_entry amount label
        memo_entry_amount_label = Label(self.left_frame, text="Amount: ")
        memo_entry_amount_label.grid(column=1, row=4)

        # Creating memo_entry amount entry
        self.memo_entry_amount_entry.grid(column=2, row=4)

        # Creating Part Label
        self.use_partial_amount()

        # Creating date label
        date_label = Label(self.left_frame, text="Date: ")
        date_label.grid(column=1, row=6)

        # Creating date entry
        date_entry = Entry(self.left_frame, width=50)
        date_entry.insert(0, self.date)
        date_entry.grid(column=2, row=6)

        # Creating date label
        total_label = Label(self.right_frame, text="Total Outstanding: INR{}".format(str(self.total_outstanding())))
        total_label.pack(side=TOP)

        self.partial_mode_radiobutton()
        self.create_check_frame()

        # '''BOTTOM FRAME '''

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create",
                               command=lambda: self.create_button(
                                   memo_number_entry.get(),
                                   self.memo_entry_amount_entry.get(),
                                   date_entry.get()))
        create_button.grid(column=0, row=0, ipadx=20)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back_button())
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        # '''FRAME PLACEMENT '''

        self.top_frame.grid(column=0, row=0)

        self.main_frame.grid(column=0, row=1)

        self.radio_frame.grid(column=0, row=0)

        self.left_frame.grid(column=0, row=2)

        self.use_partial_frame.grid(column=0, row=3)

        self.right_frame.grid(column=1, row=0, rowspan=3, sticky=NSEW)

        self.bottom_frame.grid(column=0, row=2)

    def create_check_frame(self):

        self.right_frame = Frame(self.main_frame, highlightbackground="black",
                                 highlightcolor="black", highlightthickness=1)

        # Creating Bill Number Label
        bill_number = Label(self.right_frame, text="Pending Bill-Numbers: ")
        bill_number.pack(side=TOP)

        for pick in self.pending_bill:
            text = "#" + str(pick.bill_number) + ", Amount: INR " + str(
                pick.amount - pick.part_payment)
            if pick.status == "N":
                self.checkbutton(text, "red")
            elif pick.status == "P":
                text = text + "  |  Part Paid: INR {}".format(pick.part_payment)
                self.checkbutton(text, "blue")

        self.right_frame.grid(column=1, row=0, rowspan=3, sticky=NSEW)

    def show_main_window(self) -> None:
        self.create_main_frame()
        self.window.mainloop()

    def radio_button_maker(self):
        radio_tracker = IntVar()

        for (text, value) in self.radio_options.items():
            Radiobutton(self.radio_frame, text=text, variable=radio_tracker,
                        value=value, command=lambda: self.mode_selection(radio_tracker)).pack(side=LEFT, ipady=5, padx=30)

    def checkbutton(self, text: str, background: str):

        var = IntVar()
        chk = Checkbutton(self.right_frame, text=text, variable=var,
                          fg=background)
        var.trace("w", lambda *args, v=var: self.callback(var, chk))
        chk.pack(side=TOP)

    # Implement the usage of Partial Payments
    def use_partial_amount(self):
        # Creating Partial amount Label
        partial_label = Label(self.use_partial_frame, text="Partial Amount: {}".format(
            self.partial_amount))

        use_tracker = IntVar()
        use_checkbox = Checkbutton(self.use_partial_frame, text= "Use Partial amount?", variable=use_tracker,
                                   fg="blue")

        use_tracker.trace("w", lambda *args, v=use_tracker: self.use_partial_listener(use_tracker))

        partial_label.grid(column=1, row=5)
        use_checkbox.grid(column=1, row=6)

    def create_button(self, memo_number: str, amount: str, date: str) -> None:

        try:
            int_amount = int(amount)
            int_memo_number = int(memo_number)

            if self.selected_mode == 1:
                self.memo_full(int_memo_number, int_amount, date)
            elif self.selected_mode == 2:
                if self.selected_partial == 1:
                    self.memo_partial_bill(int_memo_number, int_amount, date)
                else:
                    self.memo_partial_random(int_memo_number, int_amount, date)
            elif self.selected_mode == 3:
                self.memo_goods_return(int_memo_number, int_amount, date)
            else:
                messagebox.showwarning(title="Error",
                                       message=
                                       "Please Select a Payment Option.")

        except ValueError:
            messagebox.showwarning(title="Error",
                                   message=
                                   "Invalid Amount or Memo Number Entered")

    def memo_full(self, memo_number: int, amount: int, date: str):

        if amount < self.total:
            messagebox.showwarning(title="Error",
                                   message=
                                   "The minimum amount paid must be INR{}".format(self.total))
        else:
            if self.use_partial == 1:
                Lists.use_partial_amount(self.supplier_name, self.party_name,
                                         amount)

            MemoEntry.call_full(memo_number, self.supplier_name,
                                self.party_name,
                                amount, date, self.selected_bills)

    def memo_partial_bill(self, memo_number: int, amount: int, date: str):

        if amount < 0:
            messagebox.showwarning(title="Error",
                                   message="Amount should be more than INR 0")
        else:
            if self.use_partial == 1:
                Lists.use_partial_amount(self.supplier_name, self.party_name,
                                         amount)
            MemoEntry.call_partial_bill(memo_number, self.supplier_name,
                                        self.party_name,
                                        amount, date, self.selected_bills)
        '''
        elif amount > self.selected_bills[0].amount:
            messagebox.showwarning(title="Error",
                                   message="Amount should be LESS than Selected"
                                           "Bill total: INR{}".
                                   format(self.selected_bills[0].amount))
        '''

    def memo_partial_random(self, memo_number: int, amount: int, date: str):

        if amount < 0:
            messagebox.showwarning(title="Error",
                                   message="Amount should be more than INR 0")
        else:
            MemoEntry.call_partial_random(memo_number, self.supplier_name,
                                          self.party_name,
                                          amount, date, self.selected_bills)

    def memo_goods_return(self, memo_number: int, amount: int, date: str):

        if amount < 0:
            messagebox.showwarning(title="Error",
                                   message="Amount should be more than INR 0")
        else:
            MemoEntry.call_gr(memo_number, self.supplier_name,
                              self.party_name,
                              amount, date, self.selected_bills)

    def back_button(self)-> None:
        self.window.destroy()
        party_selector.execute(self.supplier_name, "Memo Entry")

    def callback(self, variable: IntVar, chk: Checkbutton):

        temp_amount = (((chk.cget("text")).split("INR"))[1]).strip()
        amount = int(temp_amount.split(" ")[0])
        bill_number = int((((chk.cget("text")).split(" "))[0])[1:-1])

        if variable.get() == 0:
            self.total = self.total - amount
            self.selected_bills.remove(bill_number)
        else:
            self.total += amount
            self.selected_bills.append(bill_number)

        self.memo_entry_amount_entry.delete(0, "end")
        self.memo_entry_amount_entry.insert(0, str(self.total))

    def use_partial_listener(self, variable: IntVar):

        self.use_partial = variable.get()

    def mode_selection(self, variable: IntVar):
        current_choice = variable.get()
        self.selected_mode = int(current_choice)
        self.show_partial_options()
        self.total = 0
        self.selected_bills = []
        self.memo_entry_amount_entry.delete(0, "end")
        self.memo_entry_amount_entry.insert(0, str(self.total))
        self.right_frame.destroy()
        self.create_check_frame()

    def partial_mode_radiobutton(self):
        radio_tracker = IntVar()

        # Creating Partial Label
        Label(self.partial_frame, text="Partial Payment Option: ").pack(side=LEFT)

        for (text, value) in self.partial_options.items():
            Radiobutton(self.partial_frame, text=text, variable=radio_tracker,
                        value=value, command=lambda: self.partial_mode_selection(radio_tracker)).pack(side=LEFT, ipady=5, padx=30)

    def partial_mode_selection(self, radio_tracker: IntVar):
        current_choice = radio_tracker.get()
        self.selected_partial = current_choice

    def show_partial_options(self):

        if self.selected_mode == 2:
            self.partial_frame.grid(column=0, row=1, pady=5)
        else:
            self.partial_frame.grid_forget()

    def total_outstanding(self)-> int:
        total = 0
        for bill in self.pending_bill:
            if bill.status == "N" or bill.status == "P":
                total += bill.amount
        return total


def execute(supplier: str, party: str) -> None:
    new_window = AddMemoEntry(supplier, party)
    new_window.show_main_window()




