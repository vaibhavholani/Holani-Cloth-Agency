"""
==== Description ====
This class is used to represent a register entry. A register entry is made when
the bill for an order is received.

"""

from __future__ import annotations
from Database import Lists
from typing import List
from Indivijuval import Supplier, Party
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
    # do we decided the bill number or is it predefined
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
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.payment_date = []
        self.gr_date = []
        self.status = "N"
        self.part_payment = 0
        self.gr_amount = 0

    def trial_status(self):
        self.status = "P"


def call(bill: int, amount: int, supplier: str, party: str,  date: str) -> RegisterEntry:
    register = RegisterEntry(bill, amount, supplier, party, date)
    Lists.insert_data(register)
    return register









