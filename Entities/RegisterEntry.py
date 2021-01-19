"""
==== Description ====
This class is used to represent a register entry. A register entry is made when
the bill for an order is received.

"""

from __future__ import annotations
from Database import retrieve_indivijual, insert_register_entry
from typing import List
import datetime


class RegisterEntry:

    """
    A class that represents a register entry


    ===Attributes===

    bill_number: a unique number that links a RegisterEntry to a MemoEntry
    amount: the amount for which the party has received an order
    date: the date when the bill is received
    supplier: the full name of the supplier
    party: the full name of the party

    """

    bill_number: int
    amount: int
    date: datetime
    payment_date: List[datetime]
    gr_date: List[datetime]
    supplier_name: str
    party_name: str
    goods_return: int

    def __init__(self, bill: int, amount: int, supplier: str, party: str,
                 date: str) -> None:

        self.bill_number = bill
        self.amount = amount
        self.party_name = party
        self.supplier_name = supplier
        self.supplier_id = int(retrieve_indivijual.get_supplier_id_by_name(self.supplier_name))
        self.party_id = int(retrieve_indivijual.get_party_id_by_name(self.party_name))
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")

        # Deduction AMOUNT and Deduction PERCENT
        self.gr_amount = 0
        self.d_amount = 0
        self.d_percent = 0

        self.status = "N"
        self.part_payment = 0


def call(bill: int, amount: int, supplier: str, party: str,  date: str) -> RegisterEntry:
    register = RegisterEntry(bill, amount, supplier, party, date)
    if insert_register_entry.check_new_register(register):
        insert_register_entry.insert_register_entry(register)
    return register









