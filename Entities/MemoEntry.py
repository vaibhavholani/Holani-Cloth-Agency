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

    amount: the amount for which the party has received an order
    date: the date

    """

    supplier_name: str
    party_name: str
    amount: int
    date: str

    def __init__(self, amount: int, party: str, supplier: str,
                 date: str) -> None:

        self.supplier_name = supplier
        self.party_name = party
        self.amount = amount
        self.date = date


def call(supplier: str, party: str, amount: int, date: str) -> MemoEntry:
    return MemoEntry(amount, party, supplier, date)
