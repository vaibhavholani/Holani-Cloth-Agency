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
    date: datetime
    supplier: Supplier
    party: Party

    def __init__(self, bill: int, amount: int, party: Party, supplier: Supplier):
        self.bill_number = bill
        self.amount = amount
        self.party = party
        self.supplier = supplier
        self.date = datetime.date.today()





