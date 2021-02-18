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
        self.window.bind("<Escape>", lambda event: self.back_button())
        # Creating the main frame
        self.main_frame = Frame(self.window)

        # Creating the main-right frame
        self.main_right_frame = Frame(self.window)

        # Creating a list of Selected Supplier Names
        self.selected_names = []
        self.selected_ids = []

        # Creating bottom_frame
        self.bottom_frame = Frame(self.window)

        self.master = retrieve_indivijual.get_all_supplier_names()
        self.master_id = retrieve_indivijual.get_all_supplier_id()

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
        listbox.bind("<Return>", func=lambda event: self.on_select_add(
            listbox.get(listbox.curselection()), search_entry))
        search_entry.bind("<Return>", lambda event: self.listbox_smart_select(listbox))
        listbox.bind("<Down>", lambda event: self.down_arrow(listbox))
        listbox.bind("<Up>", lambda event: self.up_arrow(listbox))

        # Creating back button
        back_button = Button(self.bottom_frame, text="<<Back",
                             command=lambda: self.back_button())
        back_button.grid(column=2, row=1, columnspan=2, ipadx=20, padx=90, ipady=10, pady=10)

        # Creating Add Button
        add_button = Button(self.bottom_frame, text="Add",
                            command=lambda: self.on_select_add(
                                listbox.get(listbox.curselection()), search_entry))

        add_button.grid(column=0, row=0, ipadx=20, padx=90, ipady=10,
                        pady=10)

        # Creating Select Button
        select_button = Button(self.bottom_frame, text="Select",
                               command=lambda: self.on_select())
        # self.window.bind('s', lambda event: self.on_select())
        select_button.grid(column=0, row=1, columnspan=2, ipadx=20, padx=90, ipady=10,
                           pady=10)

        # Creating Select All Button
        select_all_button = Button(self.bottom_frame, text="Select All",
                                   command=lambda: self.add_all())
        # self.window.bind('a', lambda event: self.add_all())
        select_all_button.grid(column=2, row=0, ipadx=20, padx=90, ipady=10,
                               pady=10)

        # Creating Select All Button
        delete_all_button = Button(self.bottom_frame, text="Delete All",
                                   command=lambda: self.del_all())
        # self.window.bind('d', lambda event: self.del_all())
        delete_all_button.grid(column=3, row=0, ipadx=20, padx=90, ipady=10,
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
            [element for element in self.master if search.upper() in element]

        listbox = self.main_frame.nametowidget("listbox")
        listbox.delete(0, END)
        listbox.insert(END, *self.suppliers)

    def down_arrow(self, listbox: Listbox):
        curr = listbox.curselection()[0]
        if curr < listbox.size() - 1:
            curr += 1
        else:
            curr = 0
        listbox.selection_clear(0, END)
        listbox.select_set(curr)

    def up_arrow(self, listbox: Listbox):
        curr = listbox.curselection()[0]
        if curr > 0:
            curr -= 1
        else:
            curr = listbox.size() - 1
        listbox.selection_clear(0, END)
        listbox.select_set(curr)

    def listbox_smart_select(self, listbox: Listbox):
        listbox.focus()
        listbox.select_set(0)
        listbox.activate(0)

    def on_select_add(self, select: str, search_entry: Entry):
        search_entry.focus()
        index = self.master.index(select)
        if select.upper() not in self.selected_names:
            bisect.insort(self.selected_names, select)
            print(index)
            print(self.master_id[index])
            bisect.insort(self.selected_ids, self.master_id[index])
            listbox2 = self.main_right_frame.nametowidget("listbox2")
            listbox2.delete(0, END)
            listbox2.insert(END, *self.selected_names)

    def on_select_del(self, select: str):
        index = self.master.index(select)
        self.selected_ids.remove(self.master_id[index])
        self.selected_names.remove(select)
        listbox2 = self.main_right_frame.nametowidget("listbox2")
        listbox2.delete(0, END)
        listbox2.insert(END, *self.selected_names)

    def add_all(self):
        self.selected_names = self.master.copy()
        self.selected_ids = self.master_id.copy()
        listbox2 = self.main_right_frame.nametowidget("listbox2")
        listbox2.delete(0, END)
        listbox2.insert(END, *self.selected_names)

    def del_all(self):
        self.selected_names = []
        self.selected_ids = []
        listbox2 = self.main_right_frame.nametowidget("listbox2")
        listbox2.delete(0, END)
        listbox2.insert(END, *self.selected_names)

    def on_select(self):
        if len(self.selected_names) == 0:
            messagebox.showwarning(title="No supplier Selected", message="Please select a supplier")
        else:
            self.window.destroy()
            multiple_party_selector.execute(self.start_date, self.end_date, self.selected_ids)

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
