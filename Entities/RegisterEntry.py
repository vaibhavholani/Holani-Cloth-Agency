"""
==== Description ====
This class is used to represent a register entry. A register entry is made when
the bill for an order is received.

"""

from __future__ import annotations
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
    date: str
    supplier_name: str
    party_name: str

    def __init__(self, bill: int, amount: int, party: str, supplier: str,
                 date: str) -> None:
        self.bill_number = bill
        self.amount = amount
        self.party_name = party
        self.supplier_name = supplier
        self.date = date
        self.status = "N"
        self.part_payment = 0


def call(bill: int, amount: int, party: str, supplier: str,  date: str) -> RegisterEntry:
    return RegisterEntry(bill, amount, party, supplier, date)




