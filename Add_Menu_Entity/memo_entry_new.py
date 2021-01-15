"""
==== Description ====
This class is used to acquire information to add memo_entry to the
database.

"""
from __future__ import annotations
from Add_Menu_Entity import party_selector, ScrollableFrame
from typing import List, Tuple
from Entities import MemoEntry
from Database import retrieve_register_entry, retrieve_indivijual, retrieve_partial_payment, retrieve_memo_entry
from Database import update_partial_amount
from Main import MainMenu
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

    # Setting Constant Options
    radio_options = {"Full": "1", "Partial": "2", "Goods Return": "3"}
    partial_options = {"In-Bill": "1", "No-bill": "2"}

    def __init__(self, supplier: str, party: str, date1: str,
                 date2: str, date3: st, memo_number: int = 0) -> None:
        """
        Creating T-kinter window
        """
        # The main window
        self.window = tkinter.Tk()
        self.window.title("Add Memo entry")
        self.window.geometry("1500x600")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Creating top frame
        self.top_frame = Frame(self.window, highlightbackground="black",
                               highlightcolor="black",
                               highlightthickness=1, width=100)

        # Creating the main frame
        self.main_frame = Frame(self.window)

        # Creating the main-left frame
        self.left_frame = Frame(self.main_frame)

        # Creating the main-right frame
        self.right_frame = Frame(self.main_frame)
        self.scrollable_body = ScrollableFrame.Scrollable(self.right_frame)

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

        # Setting Supplier and Party ID
        self.supplier_id = int(retrieve_indivijual.get_supplier_id_by_name(self.supplier_name))
        self.party_id = int(retrieve_indivijual.get_party_id_by_name(self.party_name))

        # Extend Memo Options
        self.memo_number_entry = Entry(self.left_frame, width=50)
        # Creating memo_number entry
        self.memo_number_entry.grid(column=2, row=3, columnspan=5)
        self.memo_number_entry.insert(0, str(memo_number))

        # Date Entry
        self.date_entry1 = Entry(self.left_frame, width=10)
        self.date_entry1.insert(0, str(date1))
        Label(self.left_frame, text=" / ").grid(column=3, row=4)
        Label(self.left_frame, text=" / ").grid(column=5, row=4)
        self.date_entry1.grid(column=2, row=4)
        self.date_entry2 = Entry(self.left_frame, width=10)
        self.date_entry2.insert(0, str(date2))
        self.date_entry2.grid(column=4, row=4)
        self.date_entry3 = Entry(self.left_frame, width=20)
        self.date_entry3.insert(0, str(date3))
        self.date_entry3.grid(column=6, row=4)

        # Setting Dynamic Entry for Memo Entry amount
        self.memo_entry_amount_entry = Entry(self.left_frame, width=50)
        self.memo_entry_amount_entry.insert(0, str(self.total))


        # Creating Selected bills list
        self.selected_bills = []

        # Selected Mode Tracker ( Full or Partial or GR)
        self.selected_mode = 1

        # Partial Mode Tracker (Partial-in-bill or Partial-no-bill)
        self.selected_partial = 1

        # No-Bill-Partial Amount between the supplier and the party
        self.partial_amount = retrieve_partial_payment.get_partial_payment(self.supplier_id, self.party_id)

        # Use No-Bill partial tracker
        self.use_partial = 0

        # Creating pending bill list
        pending_bill_numbers = retrieve_register_entry.get_pending_bill_numbers(self.supplier_id, self.party_id)
        self.pending_bills = retrieve_register_entry.get_register_entry_bill_numbers\
            (self.supplier_id, self.party_id, pending_bill_numbers)

        # Getting a List of all bank names
        self.bank_names = retrieve_indivijual.get_all_bank_names()
        self.bank_tracker = StringVar(self.main_frame)
        self.bank_tracker.set(self.bank_names[self.bank_names.index("Cash")])
        self.payment_info = []

    def create_main_frame(self) -> None:
        """
        Creates the main Frame!
        Contains -
        TOP FRAME (Party Name, Supplier Name)
        MAIN FRAME (Radio buttons for modes, Pending Bill List, Entry's)
        BOTTOM FRAME (back button, create button)
        """
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

        # Creating date label
        date_label = Label(self.left_frame, text="Date: ")
        date_label.grid(column=1, row=4)


        # Creating memo_entry amount label
        memo_entry_amount_label = Label(self.left_frame, text="Amount: ")
        memo_entry_amount_label.grid(column=1, row=5)

        # Creating memo_entry amount entry
        self.memo_entry_amount_entry.grid(column=2, row=5, columnspan= 5)

        # Creating Part Label
        self.use_partial_amount()

        # Creating bank_selection drop down label and list
        bank_label = Label(self.left_frame, text="Bank Name: ")
        bank_label.grid(column=1, row=6)
        bank_drop_down = OptionMenu(self.left_frame, self.bank_tracker, *self.bank_names)
        bank_drop_down.grid(column=2, row=6, columnspan= 5)

        # Creating payment cheque_number
        cheque_label = Label(self.left_frame, text="Cheque Number: ")
        cheque_label.grid(column=1, row=7)
        cheque_entry = Entry(self.left_frame, width=50)
        cheque_entry.grid(column=2, row=7, columnspan= 5)

        # Listbox scrollbar
        scrollbar = Scrollbar(self.left_frame)
        # scrollbar.grid(column=3, row=9)

        # Creating Listbox
        listbox = Listbox(self.left_frame, name="listbox", selectmode=SINGLE, yscrollcommand=scrollbar.set, width=50,
                          height=3)
        listbox.insert(END, *self.payment_info)
        listbox.grid(column=2, row = 9, columnspan=5)

        # Creating add and delete button
        add_button = Button(self.left_frame, text = "Add", command= lambda:self.add_button(self.bank_tracker.get(),
                                                                                           cheque_entry.get()))
        add_button.grid(column = 2, row = 10)

        delete_button = Button(self.left_frame, text="Delete", command= lambda: self.delete_button(listbox.get(listbox.curselection())))
        delete_button.grid(column=3, row=10)

        # Creating Deduction Detail
        add_label = Label(self.left_frame, text="Deduction Detail Percent: ")
        add_label.grid(column=1, row=11)
        add_entry = Entry(self.left_frame, width=50)
        add_entry.insert(0, str(0))
        add_entry.grid(column=2, row=11, columnspan=5)

        # Creating Deduction Detail
        deduct_label = Label(self.left_frame, text="Deduction Detail Amount: ")
        deduct_label.grid(column=1, row=12)
        deduct_entry = Entry(self.left_frame, width=50)
        deduct_entry.insert(0, str(0))
        deduct_entry.grid(column=2, row=12, columnspan=5)

        deduct_info_label = Label(self.left_frame, text = "Note: Deduction detail should only be applied to one bill at the time")


        self.partial_mode_radiobutton()
        self.create_check_frame()

        # '''BOTTOM FRAME '''

        # Creating extend memo button

        extend_button = Button(self.bottom_frame, text="Extend Memo", command=lambda: self.extend_memo(
                                   self.memo_number_entry.get(),
                                   self.memo_entry_amount_entry.get(),
                                   "{}/{}/{}".format(self.date_entry1.get(),self.date_entry2.get(),self.date_entry3.get()),
                                   deduct_entry.get(), add_entry.get() ))

        # Creating create button
        create_button = Button(self.bottom_frame, text="Create",
                               command=lambda: self.create_button(
                                   self.memo_number_entry.get(),
                                   self.memo_entry_amount_entry.get(),
                                   "{}/{}/{}".format(self.date_entry1.get(),self.date_entry2.get(),self.date_entry3.get()),
                                   deduct_entry.get(), add_entry.get()))
        create_button.grid(column=0, row=0, ipadx=20)

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back_button())
        back_button.grid(column=2, row=0, padx=90, ipadx=20)

        # Creating back button
        main_button = Button(self.bottom_frame, text="<<Main Menu",
                             command=lambda: self.back_main_button())
        main_button.grid(column=3, row=0, padx=90, ipadx=20)

        # '''FRAME PLACEMENT '''

        self.top_frame.grid(column=0, row=0)

        self.radio_frame.grid(column=0, row=0)

        self.main_frame.grid(column=0, row=1)

        self.left_frame.grid(column=0, row=2)

        self.use_partial_frame.grid(column=0, row=3)

        self.right_frame.grid(column=1, row=0, rowspan=3, sticky=NSEW)

        self.bottom_frame.grid(column=0, row=2)

    def create_check_frame(self):
        """
        Creating the frame that add all the pending bills into checkbox format which can be selected.
        """

        self.right_frame = Frame(self.main_frame)
        self.scrollable_body = ScrollableFrame.Scrollable(self.right_frame)

        # Creating Bill Number Label
        bill_number = Label(self.scrollable_body, text="Pending Bill-Numbers: ")
        bill_number.pack(side=TOP)

        # Loop to set the text of the check buttons as red, green, blue, purple
        for pick in self.pending_bills:
            text = "#" + str(pick.bill_number) + ", Amount: INR " + str(
                pick.amount - (pick.part_payment))
            if pick.status == "N":
                self.checkbutton(text, "red")
            elif pick.status == "P":
                text = text + "  |  Part Paid: INR {}".format(pick.part_payment)
                self.checkbutton(text, "blue")

        self.scrollable_body.update()

        self.right_frame.grid(column=1, row=0, rowspan=3, sticky=NSEW)

    def checkbutton(self, text: str, background: str):
        """
        Creates Check buttons for all the pending bills in the pending bill checkbox frame.
        """
        # Creating a variable to track the status of each checkbox
        var = IntVar()
        chk = Checkbutton(self.scrollable_body, text=text, variable=var,
                          fg=background)
        var.trace("w", lambda *args, v=var: self.callback(var, chk))
        chk.pack(side=TOP)

    def show_main_window(self) -> None:
        """
        Executes and runs the main window.
        """
        self.create_main_frame()
        self.window.mainloop()

    def radio_button_maker(self):
        """
        Creates radio buttons to choose between full, partial, GR
        """
        # the variable that tracks the selected mode for full, partial, GR
        radio_tracker = IntVar()

        for (text, value) in self.radio_options.items():
            Radiobutton(self.radio_frame, text=text, variable=radio_tracker,
                        value=value, command=lambda: self.mode_selection(radio_tracker)).pack(side=LEFT, ipady=5, padx=30)

    # Implement the usage of Partial Payments
    def use_partial_amount(self):
        """
        Creates the USE partial amount b/w party and supplier frame elements
            - current partial amount
            - checkbox to check if it is being used

        """
        # Creating Partial amount Label
        partial_label = Label(self.use_partial_frame, text="Partial Amount: {}".format(
            self.partial_amount))

        # tracks the status of use check_box for partial amount b/w supplier and party.
        use_tracker = IntVar()
        use_checkbox = Checkbutton(self.use_partial_frame, text= "Use Partial amount?", variable=use_tracker,
                                   fg="blue")

        use_tracker.trace("w", lambda *args, v=use_tracker: self.use_partial_listener(use_tracker))

        # placement of elements in the frame
        partial_label.grid(column=1, row=5)
        use_checkbox.grid(column=1, row=6)

    def add_button(self, bank_name: str, cheque_number: str) -> None:
        """
        Add a payment info into the list box
        """
        error = False

        if self.selected_mode != 3 and self.use_partial != 1:
            try:
                int(cheque_number)
            except ValueError:
                error = True
                success_message = False
                messagebox.showwarning(title="Error", message="Invalid Cheque Number entered")

        if not error:
            self.payment_info.append((bank_name, cheque_number))
            self.update_payment_list()

    def delete_button(self, selected_entry):
        """
        Delete a payement info from the list box
        """
        self.payment_info.remove(selected_entry)
        self.update_payment_list()


    def update_payment_list(self):
        """
        Refresh the selected options

        """
        listbox2 = self.left_frame.nametowidget("listbox")
        listbox2.delete(0, END)
        listbox2.insert(END, *self.payment_info)

    def create_button(self, memo_number: str, amount: str, date: str, d_amount: str = 0, d_percent: str = 0) -> None:
        """
        Creates the memo entry in all the modes there are i.e full, partial, GR
        """
        error = False
        success_message = True
        try:
            int(amount)
        except ValueError:
            error = True
            success_message = False
            messagebox.showwarning(title="Error", message="Invalid amount entered")

        try:
            int(memo_number)
        except ValueError:
            error = True
            success_message = False
            messagebox.showwarning(title="Error", message="Invalid Memo Number entered")

        try:
            validate(date)
        except ValueError:
            error = True
            success_message = False
            messagebox.showwarning(title="Error", message="Entered Date Should be in - DD-MM-YYYY format")

        # Check the deduction detail
        try:
            int(d_amount)
            int(d_percent)
            if int(d_percent) > 100:
                raise ValueError
        except ValueError:
            error = True
            success_message = False
            messagebox.showwarning(title="Error", message="Deduction Percent and Amount must be a number and "
                                                          "deduction percent must be less than 100.")

        try:
            if int(d_amount) != 0 and int(d_percent) != 0:
                raise ValueError
        except ValueError:
            error = True
            success_message = False
            messagebox.showwarning(title="Error", message="Both deduction detail and percentage cant be used at the "
                                                          "same time, please only use one.")

        try:
            if (int(d_amount) != 0 or int(d_percent) != 0) and len(self.selected_bills) > 1:
                raise ValueError
        except ValueError:
            error = True
            success_message = False
            messagebox.showwarning(title="Error", message="Deduction Detail can only be provided for only one bill "
                                                          "at a time. Please only select one bill.")

        # Checking if no mode is selected
        if self.selected_mode not in [1, 2, 3]:
            messagebox.showwarning(title="Error", message="Please Select a Payment Option.")
            error = True
            success_message = False

        # Check if a bank is selected
        if (self.selected_mode == 1 and len(self.payment_info) == 0 and self.use_partial == 0) or \
                (self.selected_mode == 2  and self.use_partial == 0
                 and len(self.payment_info) == 0):
            messagebox.showwarning(title="Error", message="A bank must be selected")
            error = True
            success_message = False

        if not retrieve_memo_entry.check_new_memo(int(memo_number), date, self.supplier_name, self.party_name):
            messagebox.showwarning(title="Error", message="Duplicate Memo Number Before 1 month.")
            error = True
            success_message = False

        # Amount Checks
        # Full Mode
        if self.selected_mode == 1 and int(amount) != self.total:
            messagebox.showwarning(title="Error", message="Memo amount: {} greater than sum "
                                                          "amount of bills {}".format(amount, str(self.total)))
            error = True
            success_message = False

        if self.selected_mode == 2 and self.selected_partial == 1 and int(amount) > self.total:
            messagebox.showwarning(title="Error", message="Memo amount: {} greater than max sum "
                                                          "amount of bill partial payment {}".format(amount, str(self.total)))
            error = True
            success_message = False

        # In partial amount cant be used in GR and part no bills
        if (self.selected_mode == 3 or self.selected_partial == 2) and self.use_partial == 1:
            messagebox.showwarning(title="Error", message="Partial Amount can't be used in GR or Partial No-bill Entry")
            error = True
            success_message = False

        # Proper Use of Partial Amount
        if self.use_partial == 1 and int(amount) > self.partial_amount and len(self.payment_info) == 0:
            messagebox.showwarning(title="Error",
                                    message="Total Memo Amount {} is more than total partial amount {}. "
                                            "Must add more payment information! ".format(self.total,
                                                                                        self.partial_amount))
            error = True
            success_message = False

        # Restricting Partial bills entries to only one
        if self.selected_mode == 2 and self.selected_partial == 1 and len(self.selected_bills) > 1:
            messagebox.showwarning(title="Error",
                                   message= "Partial Payment In-Bill can only be made into one bill at a time")
            error = True
            success_message = False


        # if there is a error then execution
        if not error:
            int_amount = int(amount)
            int_memo_number = int(memo_number)
            d_amount = int(d_amount)
            d_percent = int(d_percent)
            """Separate execution of different modes"""
            if self.selected_mode == 1:
                # Full Mode
                self.memo_full(int_memo_number, int_amount, date, self.payment_info, d_amount, d_percent)
            elif self.selected_mode == 2:
                # Partial Mode
                if self.selected_partial == 1:
                    # Partial In-bill Mode
                    self.memo_partial_bill(int_memo_number, int_amount, date, self.payment_info, d_amount, d_percent)
                else:
                    # Partial No-bill Mode
                    self.memo_partial_random(int_memo_number, int_amount, date, self.payment_info)
            elif self.selected_mode == 3:
                # Goods Return Mode
                self.memo_goods_return(int_memo_number, int_amount, date, self.payment_info)

        """Displaying success message if memo created"""
        if success_message:
            # Showing Completion Message
            messagebox.showinfo(title="Complete", message="Memo Added!")

            # Updating UI elements
            self.refresh_window()

    def memo_full(self, memo_number: int, amount: int, date: str, payment_info: List[Tuple], d_amount: int, d_percent: int):
        """
        Creating memos on Full Payment Mode
        """
        # Checking if enough amount is paid
        if amount < self.total:
            messagebox.showwarning(title="Error",
                                   message=
                                   "The minimum amount paid must be INR{}".format(self.total))
        else:
            # Check if the partial_amount between supplier and party is being used
            use_amount = amount
            if d_amount != 0:
                use_amount = amount - d_amount
            elif d_percent != 0:
                use_amount = amount - ((d_percent/100)*amount)
            if self.use_partial == 1:
                update_partial_amount.use_partial_amount(self.supplier_id, self.party_id, use_amount)

            MemoEntry.call_full(memo_number, self.supplier_name,
                                self.party_name,
                                use_amount, date, payment_info, self.selected_bills, d_amount, d_percent)

    def memo_partial_bill(self, memo_number: int, amount: int, date: str, payment_info: List[Tuple], d_amount: int, d_percent: int):
        """
        Creating memos on partial in-bill Payment Mode
        """
        # Checking if enough amount is paid
        if amount < 0:
            messagebox.showwarning(title="Error",
                                   message="Amount should be more than INR 0")
        else:
            # Check if the partial_amount between supplier and party is being used
            use_amount = amount
            if d_amount != 0:
                use_amount = amount - d_amount
            elif d_percent != 0:
                use_amount = amount - ((d_percent / 100) * amount)
            if self.use_partial == 1:
                update_partial_amount.use_partial_amount(self.supplier_id, self.party_id, use_amount)

            MemoEntry.call_partial_bill(memo_number, self.supplier_name,
                                        self.party_name,
                                        use_amount, date, payment_info, self.selected_bills, d_amount, d_percent)

    def memo_partial_random(self, memo_number: int, amount: int, date: str, payment_info: List[Tuple]):
        """
        Creating memos on partial no-bill Payment Mode
        """

        if amount < 0:
            messagebox.showwarning(title="Error",
                                   message="Amount should be more than INR 0")
        else:
            MemoEntry.call_partial_random(memo_number, self.supplier_name,
                                          self.party_name,
                                          amount, date, payment_info, self.selected_bills)

    def memo_goods_return(self, memo_number: int, amount: int, date: str, payment_info: List[Tuple]):
        """
        Creating memos goods return Mode
        """

        if amount < 0:
            messagebox.showwarning(title="Error",
                                   message="Amount should be more than INR 0")
        else:
            MemoEntry.call_gr(memo_number, self.supplier_name,
                              self.party_name,
                              amount, date, payment_info, self.selected_bills)

    def back_button(self) -> None:
        """
        Takes back to the previous window
        """
        self.window.destroy()
        party_selector.execute(self.supplier_name, "Memo Entry")

    def back_main_button(self) -> None:
        """
        Go back to the main menu
        """
        self.window.destroy()
        MainMenu.execute()


    def extend_memo(self, memo_number: str, amount: str, date: str, bank_name: str, cheque_number: str):
        """
        Implements the use of extend memo option
        """
        self.window.destroy()
        self.create_button(memo_number, amount, date, bank_name, cheque_number)
        execute(self.supplier_name, self.party_name)

    def callback(self, variable: IntVar, chk: Checkbutton):
        """
        Updating the contents of the entry amount on the basis of the selected bills
        """
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
        """
        Updating the current selected option for use partial no bill and in bill
        """
        self.use_partial = variable.get()

    def mode_selection(self, variable: IntVar):
        """
        Checks the current mode selected by the user, and updated the amount option
        """
        current_choice = variable.get()
        self.selected_mode = int(current_choice)

        # Checking if the partial amount needs to be used, and showing options accordingly
        self.show_partial_options()

        self.total = 0

        # unchecking all the selected bills
        self.selected_bills = []

        # Reset entry Amount to 0 then the current total
        self.memo_entry_amount_entry.delete(0, "end")
        self.memo_entry_amount_entry.insert(0, str(self.total))
        self.right_frame.destroy()
        self.create_check_frame()

    def partial_mode_radiobutton(self):
        """
        Creates radio button to select partial in-bill or no-bill options.
        """
        radio_tracker = IntVar()

        # Creating Partial Label
        Label(self.partial_frame, text="Partial Payment Option: ").pack(side=LEFT)

        for (text, value) in self.partial_options.items():
            Radiobutton(self.partial_frame, text=text, variable=radio_tracker,
                        value=value, command=lambda: self.partial_mode_selection(radio_tracker)).pack(side=LEFT, ipady=5, padx=30)

    def partial_mode_selection(self, radio_tracker: IntVar):
        """
        Keeps track of which partial mode is selected : partial in-bill or no-bill
        """
        current_choice = radio_tracker.get()
        self.selected_partial = current_choice

    def show_partial_options(self):
        """
        Checks if the partial mode is selected, and if it is shows the partial in-bill and no-bill options.
        """
        if self.selected_mode == 2:
            self.partial_frame.grid(column=0, row=1, pady=5)
        else:
            self.partial_frame.grid_forget()

    def total_outstanding(self) -> int:
        """
        Gives the total amount that the party needs to pay the supplier
        """
        total = 0
        for bill in self.pending_bills:
            if bill.status in ["N", "P"]:
                total += (bill.amount - bill.part_payment)
        return total

    def set_extend(self, memo_number, memo_date):
        self.memo_number_entry.insert(0, str(memo_number))
        self.date_entry.insert(0, memo_date)

    def refresh_window(self) -> None:
        """
        Refreshes the window to show updated results
        """
        memo_number = self.memo_number_entry.get()
        memo_date1 = self.date_entry1.get()
        memo_date2 = self.date_entry2.get()
        memo_date3 = self.date_entry3.get()
        self.window.destroy()
        execute(self.supplier_name, self.party_name, memo_date1, memo_date2, memo_date3, memo_number)


def validate(date_text: str):
    """
    Used to validate date format
    """
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD/MM/YYYY")


def execute(supplier: str, party: str, date1: str = str(datetime.date.today().day),
                 date2: str = datetime.date.today().month, date3: str = datetime.date.today().year, memo_number: int = 0 ) -> MemoEntry:
    # Setting Date and time
    new_window = AddMemoEntry(supplier, party, date1, date2, date3, memo_number)
    new_window.show_main_window()
    # new_window.set_extend(memo_number, memo_date)
    return new_window



