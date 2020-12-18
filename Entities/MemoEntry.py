"""
==== Description ====
This class is used to represent a memo entry.

"""

from __future__ import annotations
from typing import List
import datetime
from Database import Lists, retrieve_memo_entry, retrieve_indivijual, insert_memo_entry
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
    selected_bills: List

    def __init__(self, memo_number: int, amount: int, party: str, supplier: str,
                 date: str, selected_bills: List[RegisterEntry], mode: str) -> None:

        self.memo_number = memo_number
        self.supplier_name = supplier
        self.party_name = party
        self.supplier_id = int(retrieve_indivijual.get_supplier_id_by_name(self.supplier_name))
        self.party_id = int(retrieve_indivijual.get_party_id_by_name(self.party_name))
        self.amount = amount
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.mode = mode
        self.selected_bills = Lists.re_bill_numbers(self.supplier_name, self.party_name, selected_bills)
        self.insert_memo_database()
        self.memo_id = self.get_memo_id()

    def insert_memo_database(self) -> None:
        """
        Adds memo to the database if the memo is new.
        """
        if retrieve_memo_entry.check_new_memo(self):
            insert_memo_entry.insert_memo_entry(self)

    def inset_memo_bill_database(self, bills: RegisterEntry) -> None:
        """
        Adds bills to the attached memo to the database.
        """

        MemoBill.call(self.memo_id, bills.bill_number, bills.amount, bills.status)

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
            bills.payment_date.append(self.date)
            self.inset_memo_bill_database(bills)

    def partial_payment_bill(self) -> None:
        """
        Used to complete partial payment for bill(s)
        """

        # Loop to update the status of the selected bills
        for bills in self.selected_bills:
            if bills.status == "P" and bills.amount - self.amount:
                bills.status = "F"
            elif bills.status == "N":
                bills.status = "P"
            elif bills.status == "PG" or bills.status == "G":
                bills.status = "PG"

            bills.part_payment = self.amount
            bills.payment_date.append(self.date)
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
        MemoBill.call(self.memo_id, 0, self.amount, "PR")

    def goods_return(self) -> None:
        """
        Adds goods return to the selected bill(s).
        """

        # Loop to update the status of the selected bills
        for bills in self.selected_bills:
            if (bills.status == "P" or bills.status == "PG") and \
                    bills.amount-self.amount:
                bills.status = "F"
            elif bills.status == "P" or bills.status == "PG":
                bills.status = "PG"
            elif bills.status == "N":
                bills.status = "G"
            bills.gr_amount = bills.gr_amount + self.amount
            bills.gr_date.append(self.date)
            self.inset_memo_bill_database(bills)


def call_full(memo_number: int, supplier: str, party: str, amount: int,
              date: str,
              selected_bills: List[RegisterEntry]) -> None:

    """
    Call for full payment of the selected bill(s)
    """

    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Full")
    memo.full_payment()


def call_partial_bill(memo_number: int, supplier: str, party: str, amount: int,
                      date: str,
                      selected_bills: List[RegisterEntry]) -> None:
    """
    Call for partial payment of the selected bill(s)
    """

    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Part Bill")
    memo.partial_payment_bill()


def call_partial_random(memo_number: int, supplier: str, party: str,
                        amount: int, date: str,
                        selected_bills: List[RegisterEntry]) -> None:
    """
    Calls to add partial_payment to the account of the supplier and party
    """
    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Part Random")
    memo.partial_payment_random()


def call_gr(memo_number: int, supplier: str, party: str, amount: int, date: str,
            selected_bills: List[RegisterEntry]) -> None:
    """
    Call for goods return on the selected bill(s)
    """

    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Good Return")
    memo.goods_return()