"""
==== Description ====
This class is used to represent a memo entry.

"""

from __future__ import annotations
from typing import List, Tuple
import datetime
from Database import Lists, retrieve_memo_entry, retrieve_indivijual, insert_memo_entry, update_register_entry
from Database import insert_register_entry, retrieve_partial_payment, update_partial_amount, insert_partial_payment
from Database import insert_gr, retrieve_gr, update_gr
from Database import retrieve_register_entry
from Entities import RegisterEntry, MemoBill


class MemoEntry:

    """
    A class that represents a memo entry

    ===Attributes===

    amount: the amount for which the party has received an order
    date: the date

    """
    memo_number: int
    supplier_name: str
    party_name: str
    amount: int
    date: datetime
    bank_name: str
    cheque_number: int
    selected_bills: List

    def __init__(self, memo_number: int, amount: int, party: str, supplier: str,
                 date: str, payment_info: List[Tuple], selected_bills: List[RegisterEntry], mode: str,
                 d_amount: int = 0, d_percent: int = 0) -> None:

        self.memo_number = memo_number
        self.supplier_name = supplier
        self.party_name = party
        self.supplier_id = int(retrieve_indivijual.get_supplier_id_by_name(self.supplier_name))
        self.party_id = int(retrieve_indivijual.get_party_id_by_name(self.party_name))
        self.amount = amount
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.date_string = date
        self.payment_info = payment_info
        self.mode = mode
        self.selected_bills = retrieve_register_entry.get_register_entry_bill_numbers\
            (self.supplier_id, self.party_id, selected_bills)
        self.insert_memo_database()
        self.memo_id = self.get_memo_id()
        self.d_amount = d_amount
        self.d_percent = d_percent

    def insert_memo_database(self) -> None:
        """
        Adds memo to the database if the memo is new.
        """
        if retrieve_memo_entry.check_add_memo(self.memo_number, self.date_string):
            insert_memo_entry.insert_memo_entry(self)
        insert_memo_entry.insert_memo_payemts(self)

    def inset_memo_bill_database(self, bills: RegisterEntry) -> None:
        """
        Adds bills to the attached memo to the database.
        """
        if not insert_register_entry.check_new_register(bills):
            update_register_entry.update_register_entry_data(bills)
        amount = self.amount
        if self.mode == "Full":
            amount = (bills.amount-bills.part_payment)
        MemoBill.call(self.memo_id, bills.bill_number, amount, bills.status)

    def get_memo_id(self) -> int:
        """
        Update memo id once the memo is added into the database.
        """
        return retrieve_memo_entry.get_id_by_memo_number(self.memo_number, self.supplier_id, self.party_id)

    def full_payment(self) -> None:
        """
        Used to complete full payment for bill(s)
        """
        # Loop to update the status of the selected bills
        for bills in self.selected_bills:
            bills.status = "F"
            bills.d_amount += self.d_amount
            bills.d_percent += self.d_percent
            self.inset_memo_bill_database(bills)

    def partial_payment_bill(self) -> None:
        """
        Used to complete partial payment for bill(s)
        """

        # Loop to update the status of the selected bills
        for bills in self.selected_bills:
            bills.d_percent += self.d_percent
            bills.d_amount += self.d_amount
            percent_amount = ((bills.d_amount/100)*bills.amount)
            if bills.status in ["P", "N", "G", "PG"] and \
                    (bills.amount - bills.part_payment - self.amount - bills.d_amount - percent_amount <= 0):
                bills.status = "F"
            elif bills.status == "N":
                bills.status = "P"
            elif bills.status == "G":
                bills.status = "PG"

            bills.part_payment = bills.part_payment + self.amount
            self.inset_memo_bill_database(bills)

    def partial_payment_random(self) -> None:
        """
        Adds partial payments without bills to the account of the supplier and party.
        """
        Lists.insert_partial_data(self.supplier_name, self.party_name, self.amount)
        # Call to log this memo_entry in memo_bills
        self.database_partial_payment()

    def database_partial_payment(self):
        """
        Store partial payments into the database
        """
        if retrieve_partial_payment.get_partial_payment(self.supplier_id, self.party_id) == -1:
            insert_partial_payment.insert_partial_payment(self)
        else:
            update_partial_amount.add_partial_amount(self.supplier_id, self.party_id, self.amount)

        MemoBill.call(self.memo_id, 0, self.amount, "PR")

    def goods_return(self) -> None:
        """
        Adds goods return to supplier party account.
        """
        for bills in self.selected_bills:
            if (bills.status == "P" or bills.status == "PG") and \
                    bills.amount - self.amount:
                bills.status = "PG"
            elif bills.status == "N":
                bills.status = "G"
            bills.gr_amount = self.amount
            bills.amount = bills.amount - self.amount
            bills.gr_amount = bills.gr_amount + self.amount
            self.inset_memo_bill_database(bills)
        # self.database_gr()

    def database_gr(self):
        """
        Add the GR entry to the database
        """
        if retrieve_gr.get_gr(self.supplier_id, self.party_id) <= 0:
            insert_gr.insert_gr(self)
        else:
            update_gr.add_gr_amount(self.supplier_id, self.party_id, self.amount)

        MemoBill.call(self.memo_id, 0, self.amount, "GR")


def call_full(memo_number: int, supplier: str, party: str, amount: int,
              date: str, payment_info: List[Tuple], selected_bills: List[RegisterEntry],
              d_amount: int, d_percent: int) -> None:
    """
    Call for full payment of the selected bill(s)
    """

    memo = MemoEntry(memo_number, amount, party, supplier, date, payment_info, selected_bills, "Full", d_amount,
                     d_percent)
    memo.full_payment()


def call_partial_bill(memo_number: int, supplier: str, party: str, amount: int,
                      date: str, payment_info: List[Tuple],
                      selected_bills: List[RegisterEntry], d_amount: int, d_percent: int) -> None:
    """
    Call for partial payment of the selected bill(s)
    """

    memo = MemoEntry(memo_number, amount, party, supplier, date, payment_info, selected_bills, "Part Bill", d_amount,
                     d_percent)
    memo.partial_payment_bill()


def call_partial_random(memo_number: int, supplier: str, party: str,
                        amount: int, date: str, payment_info: List[Tuple],
                        selected_bills: List[RegisterEntry]) -> None:
    """
    Calls to add partial_payment to the account of the supplier and party
    """
    memo = MemoEntry(memo_number, amount, party, supplier, date, payment_info, selected_bills, "Part Random")
    memo.partial_payment_random()


def call_gr(memo_number: int, supplier: str, party: str,
            amount: int, date: str, payment_info: List[Tuple],
            selected_bills: List[RegisterEntry]) -> None:
    """
    Call for goods return on the selected bill(s)
    """

    memo = MemoEntry(memo_number, amount, party, supplier, date, payment_info, selected_bills,
                     "Good Return")
    memo.goods_return()
