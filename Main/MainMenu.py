import tkinter
from tkinter import *
from Add_Menu_Entity import new_entry
from Add_Menu_Indi import Add_Menu
from View_Menu import date_selector
from Database import upload_db, db_connector, online_db_connector, download_db
from tkinter import messagebox


class MainMenu:
    """
    The first frame of the program.
    Navigate to Add Register Entry, Memo Entry
    Navigate to Add Party, Supplier, Transporter Bank
    """

    def __init__(self):
        self.window = tkinter.Tk()
        self.main_frame = Frame(self.window)
        self.window.title("Main Menu")
        self.window.geometry("500x500")
        self.window.rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

    def create_main_frame(self):

        add_entry_button = Button(self.main_frame, text="Register/Memo Entry",
                                  command=lambda: self.entry_button(),
                                  padx=10, pady=10)
        add_entity_button = Button(self.main_frame, text="Add Menu",
                                   command=lambda: self.entity_button(),
                                   padx=10, pady=10)

        view_button = Button(self.main_frame, text="View Menu",
                                   command=lambda: self.view_button(),
                                   padx=10, pady=10)

        edit_button = Button(self.main_frame, text="Edit Records",
                             padx=10, pady=10)

        upload_button = Button(self.main_frame, text="Update Database",
                               command=lambda: update_button(),
                               padx=10, pady=10)
        download_buttonn = Button(self.main_frame, text="Download from Database",
                               command=lambda: download_button(),
                               padx=10, pady=10)

        add_entry_button.grid(row=0, column=0, pady=10, padx=10)
        add_entity_button.grid(row=1, column=0, pady=10, padx=10)
        view_button.grid(row=2, column=0, pady=10, padx=10)
        edit_button.grid(row=3, column=0, pady=10, padx=10)
        upload_button.grid(row=4, column=0, pady=10, padx=10)
        download_buttonn.grid(row=5, column=0, pady=10, padx=10 )

        self.main_frame.grid(row=0, column=0)
        self.window.mainloop()

    def entry_button(self):
        self.window.destroy()
        new_entry.execute()

    def entity_button(self):
        self.window.destroy()
        Add_Menu.execute()

    def view_button(self):
        self.window.destroy()
        date_selector.execute()


def update_button():
    upload_db.update()
    messagebox.showinfo(title="Complete", message="Online Database Update Complete!")


def download_button():
    local_db = db_connector.connect()
    local_cursor = local_db.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    local_cursor.execute(query)
    local_timestamp = (local_cursor.fetchall())[0][0]
    online_cursor.execute(query)
    online_timestamp = (online_cursor.fetchall())[0][0]
    if local_timestamp >= online_timestamp:
        messagebox.showinfo(title="Up to Date", message="Database Up-to-Date")
    else:
        download_db.download()
        messagebox.showinfo(title="Update Complete", message="Update Complete")


def execute():
    window = MainMenu()
    window.create_main_frame()



