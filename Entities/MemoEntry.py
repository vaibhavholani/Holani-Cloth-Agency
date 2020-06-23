"""
==== Description ====
This class is used to represent a memo entry.

"""

from __future__ import annotations
from typing import List
import datetime
from Entities import RegisterEntry


class MemoEntry:

    """
    A class that represents a memo entry

    ===Attributes===

    bill_numbers: bill_numbers for the register entries being paid off in
        full or partial
    amount: the amount for which the party has received an order
    date: the date

    """
    bill_numbers: List
    amount: int
    date: datetime

    def __init__(self, amount: int):
        self.bill_numbers = []
        self.amount = amount
        self.date = datetime.date.today()

    def add_bill(self, bill_num: List):
        self.bill_numbers.extend(bill_num)


